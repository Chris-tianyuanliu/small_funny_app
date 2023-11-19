import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import json
import datetime


class MainFrame:
    def __init__(self):
        self.window = None
        self.input_frame = None
        self.tdee_entry = None
        self.body_fat_entry = None
        self.lean_mass_entry = None
        self.total_cal_output_label = None
        self.total_cal_output_string = None
        self.menu = None
        self.calorie = None
        self.fat = None
        self.protein = None
        self.carbohydrates = None

        self.init_window()
        self.init_data_collection()
        self.init_consumable_info_label()

    def init_window(self):
        # window
        self.window = ttk.Window(themename="journal")
        # window.attributes('-fullscreen', True)
        self.window.title("减肥计算器 Designed by 克里斯")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')

    def init_data_collection(self):
        # input field
        self.input_frame = ttk.Frame(master=self.window)
        tdee_int = tk.IntVar()
        body_fat_int = tk.IntVar()
        lean_mass_int = tk.IntVar()

        tdee_texts = ttk.Label(master=self.input_frame, text='TDEE: ', font='calibri 9 bold')
        self.tdee_entry = ttk.Entry(master=self.input_frame, textvariable=tdee_int, width=10)

        body_fat_texts = ttk.Label(master=self.input_frame, text='体脂: ', font='calibri 9 bold')
        self.body_fat_entry = ttk.Entry(master=self.input_frame, textvariable=body_fat_int, width=10)

        lean_mass_texts = ttk.Label(master=self.input_frame, text='(净)体重: ', font='calibri 9 bold')
        self.lean_mass_entry = ttk.Entry(master=self.input_frame, textvariable=lean_mass_int, width=10)

        button = ttk.Button(master=self.input_frame, text='Record', command=self.human_data_collection)


        tdee_texts.pack(side='left')
        self.tdee_entry.pack(side='left', padx= (0,50))

        body_fat_texts.pack(side='left')
        self.body_fat_entry.pack(side='left', padx= (0,50))

        lean_mass_texts.pack(side='left')
        self.lean_mass_entry.pack(side='left', padx= (0,90))

        button.pack(side='left')
        self.input_frame.pack(pady=50)


    def human_data_collection(self):
        tdee = int(self.tdee_entry.get())
        mass = int(self.lean_mass_entry.get())
        self.calorie = round(tdee*0.8, 1)
        self.fat = round(self.calorie*0.25 / 9, 1)
        self.protein = round(mass * 2.2, 1)
        self.carbohydrates = round((self.calorie - self.protein * 4 - self.fat * 9)/4, 1)

        total_display = f'您目前每日摄入热量最高为{self.calorie:.1f} cal:\n其中碳水为{self.carbohydrates:.1f}g, 脂肪为{self.fat:.1f}g, 蛋白质为{self.protein:.1f}g'

        self.total_cal_output_string.set(total_display)

        self.date = str(datetime.date.today())
        # read from json
        with open('menu.json', 'r') as openfile:
            self.menu = json.load(openfile)

        if self.menu == {}:
            self.menu[self.date] = {
                "剩余卡路里": self.calorie,
                "脂肪": self.fat,
                "碳水": self.carbohydrates,
                "蛋白质":self.protein,
                "早餐":{

                },
                "午餐":{

                },
                "晚餐":{

                },
            }

            with open("menu.json", "w") as outfile:
                json.dump(self.menu, outfile, ensure_ascii=False, indent=4)


    def init_consumable_info_label(self):
        # total_cal output label
        self.total_cal_output_string = tk.StringVar()
        self.total_cal_output_label = ttk.Label(master=self.window, 
                                text='Output', 
                                font='calibri 12', 
                                textvariable=self.total_cal_output_string)
        self.total_cal_output_label.pack(pady=5)

    # pass the data from the main frame to the menu frame    
    def return_initial_human_data(self):
        return self.calorie, self.carbohydrates, self.fat, self.protein
