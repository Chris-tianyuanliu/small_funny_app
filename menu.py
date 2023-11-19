import tkinter as tk
from tkinter import ttk
import json
import datetime

class AddMenu:
    def __init__(self, window, table, calories, carbohydrates, fat, protein):
        self.menu = None
        self.amount = None
        self.table_selection_value = None
        self.combo_selected_value = None

        self.date = str(datetime.date.today())
        self.table = table
        self.table.bind('<<TreeviewSelect>>', self.menu_selection)

        self.window = window

        # Menu Frame
        self.menu_frame = ttk.Frame(master=window)
        

        # read from json
        with open('menu.json', 'r') as openfile:
            self.menu = json.load(openfile)

        if self.menu == {}:
            self.menu[self.date] = {
                "剩余卡路里": calories,
                "脂肪": fat,
                "碳水":carbohydrates,
                "蛋白质":protein,
                "早餐":{

                },
                "午餐":{

                },
                "晚餐":{

                },
            }


        # combobox
        items = ('早餐', '午餐', '晚餐')
        self.time_string = tk.StringVar()
        self.combo = ttk.Combobox(self.menu_frame, width=5)
        self.combo['values'] = items
        self.combo.place(x=350, y=0)
        self.combo.bind('<<ComboboxSelected>>', self.set_combo_value)


        amount_int = tk.IntVar()
        amount_text = ttk.Label(master=self.menu_frame, text='数量: ', font='calibri 9 bold')
        self.amount_entry = ttk.Entry(master=self.menu_frame, textvariable=amount_int, width=10)

        amount_text.place(x=500, y=0)
        self.amount_entry.place(x=600, y=0)
        self.button = ttk.Button(master=self.menu_frame, text='Record', command=self.menu_data_collection)
        self.button.place(x=820, y=0)

        self.menu_frame.pack(side='right',padx=10)
        
        self.overall_table()
        self.init_menu()
        self.menu_display()

    def init_menu(self):
        self.menu_table = ttk.Treeview(self.menu_frame, columns=('时间',
                                                                 '食物',
                                                                 '数量',
                                                                 '热量',
                                                                 '碳水', 
                                                                 '脂肪', 
                                                                 '蛋白质'),height=30)
        self.menu_table['show'] = 'headings'
        self.menu_table.heading('时间', text='时间')
        self.menu_table.heading('食物', text='食物')
        self.menu_table.heading('数量', text='数量')
        self.menu_table.heading('热量', text='热量')
        self.menu_table.heading('碳水', text='碳水')
        self.menu_table.heading('脂肪', text='脂肪')
        self.menu_table.heading('蛋白质', text='蛋白质')

        self.menu_table.column("时间", anchor="c")  
        self.menu_table.column("食物", anchor="c")  
        self.menu_table.column("数量", anchor="c")  
        self.menu_table.column("热量", anchor="c")  
        self.menu_table.column("碳水", anchor="c")  
        self.menu_table.column("脂肪", anchor="c")  
        self.menu_table.column("蛋白质", anchor="c")  
        self.menu_table.pack(pady=(10,10))



    def menu_display(self):
        # Clear the entire table
        for item in self.menu_table.get_children():
            self.menu_table.delete(item)

        meal_list = ['早餐', '午餐', '晚餐']
        added = False
        for meal in meal_list:
            for food in self.menu[self.date][meal].keys():
                if not added:
                    self.menu_table.insert(parent='',index=tk.END, values=(meal,
                                                                           food,
                                                                           self.menu[self.date][meal][food]['数量'],
                                                                           self.menu[self.date][meal][food]['热量'],
                                                                           self.menu[self.date][meal][food]['碳水'],
                                                                           self.menu[self.date][meal][food]['脂肪'],
                                                                           self.menu[self.date][meal][food]['蛋白质']))
                    added = True
                else:

                    self.menu_table.insert(parent='',index=tk.END, values=('',
                                                                           food,
                                                                           self.menu[self.date][meal][food]['数量'],
                                                                           self.menu[self.date][meal][food]['热量'],
                                                                           self.menu[self.date][meal][food]['碳水'],
                                                                           self.menu[self.date][meal][food]['脂肪'],
                                                                           self.menu[self.date][meal][food]['蛋白质']))
            added = False


    def overall_table(self):
        self.overall = ttk.Treeview(self.menu_frame, columns=('日期', '剩余热量','剩余碳水', '剩余脂肪', '剩余蛋白质'),height=1)
        self.overall['show'] = 'headings'
        self.overall.heading('日期', text='日期')
        self.overall.heading('剩余热量', text='剩余热量')
        self.overall.heading('剩余碳水', text='剩余碳水')
        self.overall.heading('剩余脂肪', text='剩余脂肪')
        self.overall.heading('剩余蛋白质', text='剩余蛋白质')
        self.overall.column("日期", anchor="c")  
        self.overall.column("剩余热量", anchor="c")  
        self.overall.column("剩余碳水", anchor="c")  
        self.overall.column("剩余脂肪", anchor="c")  
        self.overall.column("剩余蛋白质", anchor="c")  
        self.overall.pack(pady=(70,10))
        
        self.overall.insert(parent='',index=tk.END, values=(self.date,
                                                            self.menu[self.date]['剩余卡路里'],
                                                            self.menu[self.date]['脂肪'],
                                                            self.menu[self.date]['碳水'],
                                                            self.menu[self.date]['蛋白质']))
        
    def menu_data_collection(self):
        self.amount = int(self.amount_entry.get())
        name = self.table_selection_value[0]
        carbohydate = round(self.amount * float(self.table_selection_value[1]), 2)
        fat = round(self.amount * float(self.table_selection_value[2]),2)
        protein = round(self.amount * float(self.table_selection_value[3]),2)

        self.menu[self.date][self.combo_selected_value][name] = {
            "数量": self.amount,
            "热量": round(fat*9 + carbohydate*4 + protein*4,2),
            "脂肪": round(fat,2),
            "碳水": round(carbohydate,2),
            "蛋白质": round(protein,2),
            
        }

        # 总数量减去加入的食物
        self.menu[self.date]["脂肪"] -= round(fat,2)
        self.menu[self.date]["蛋白质"] -= round(protein,2)
        self.menu[self.date]["碳水"] -= round(carbohydate,2)
        self.menu[self.date]["剩余卡路里"] -= round(fat*9 + carbohydate*4 + protein*4,2)

        self.menu_display()
        
        rows = self.overall.get_children()
        self.overall.item(rows[0], values=(self.date,
                                           round(self.menu[self.date]["剩余卡路里"],2),
                                           round(self.menu[self.date]["碳水"],2),
                                           round(self.menu[self.date]["脂肪"],2),
                                           round(self.menu[self.date]["蛋白质"]),2))

        with open("menu.json", "w") as outfile:
            json.dump(self.menu, outfile, ensure_ascii=False, indent=4)


    def menu_selection(self,event):
        for i in self.table.selection():
            self.table_selection_value = self.table.item(i)['values']

    def set_combo_value(self,event):
        self.combo_selected_value=self.combo.get()
