import tkinter as tk
from tkinter import ttk
import json
class AddDatabase:
    def __init__(self, window):
        self.data = None
        self.table = None

        # Table Frame
        self.table_frame = ttk.Frame(master=window)
        
        # self.table_frame.pack(side='left',padx=10, pady=10, anchor='s')
        self.init_food_collection()
        self.init_food_table()
        self.table_frame.pack(side='left',padx=10, pady=10, anchor='s')



        self.table.bind('<Delete>', self.delete_items)

    def init_food_table(self):
        
        # Table String
        self.table_string = tk.StringVar()
        self.table_label = ttk.Label(master=self.table_frame, 
                                text='Output', 
                                font='calibri 12', 
                                textvariable=self.table_string)
        self.table_label.pack(pady=(10,0))
        self.table_string.set("食物数据库")


        # treeview
        self.table = ttk.Treeview(self.table_frame, columns=('名字', '碳水', '脂肪', '蛋白质'),height=20)
        self.table['show'] = 'headings'
        self.table.heading('名字', text='食物名称')
        self.table.heading('碳水', text='碳水')
        self.table.heading('脂肪', text='脂肪')
        self.table.heading('蛋白质', text='蛋白质')
        self.table.column("名字", anchor="c")  
        self.table.column("碳水", anchor="c")  
        self.table.column("脂肪", anchor="c")  
        self.table.column("蛋白质", anchor="c")  
        self.table.pack(pady=(10,10))

        with open('database.json', 'r') as openfile:
 
            # Reading from json file
            self.data = json.load(openfile)
        for key in self.data.keys():
            self.table.insert(parent='',index=tk.END, values=(key, 
                                                              self.data[key]['碳水'],
                                                              self.data[key]['脂肪'],
                                                              self.data[key]['蛋白质']))

        
    def delete_items(self,event):
        for i in self.table.selection():
            self.table.delete(i)


    def init_food_collection(self):

        food_name = tk.StringVar()
        food_unit = tk.DoubleVar()
        food_carbohydate = tk.DoubleVar()
        food_fat = tk.DoubleVar()
        food_protein = tk.DoubleVar()

        food_name_texts = ttk.Label(master=self.table_frame, text='食物名称: ', font='calibri 9 bold')
        self.food_name_entry = ttk.Entry(master=self.table_frame, textvariable=food_name, width=10)

        food_unit_texts = ttk.Label(master=self.table_frame, text='食物单位量: ', font='calibri 9 bold')
        self.food_unit_entry = ttk.Entry(master=self.table_frame, textvariable=food_unit, width=10)

        food_carbohydate_texts = ttk.Label(master=self.table_frame, text='单位所含碳水: ', font='calibri 9 bold')
        self.food_carbohydate_entry = ttk.Entry(master=self.table_frame, textvariable=food_fat, width=10)

        food_fat_texts = ttk.Label(master=self.table_frame, text='单位所含脂肪: ', font='calibri 9 bold')
        self.food_fat_texts_entry = ttk.Entry(master=self.table_frame, textvariable=food_carbohydate, width=10)

        food_protein_texts = ttk.Label(master=self.table_frame, text='单位所含蛋白质: ', font='calibri 9 bold')
        self.food_protein_texts_entry = ttk.Entry(master=self.table_frame, textvariable=food_protein, width=10)

        button = ttk.Button(master=self.table_frame, text='Record', command=self.add_food_database)


        food_name_texts.pack(pady=(10,10),side='top', anchor='w')
        self.food_name_entry.pack(padx= (0,50),side='top',anchor='w')

        food_unit_texts.pack(pady=(10,10), side='top', anchor='w')
        self.food_unit_entry.pack( padx= (0,50), side='top', anchor='w')

        food_carbohydate_texts.pack(pady=(10,10), side='top', anchor='w')
        self.food_carbohydate_entry.pack( padx= (0,50), side='top', anchor='w')

        food_fat_texts.pack(pady=(10,10), side='top', anchor='w')
        self.food_fat_texts_entry.pack( padx= (0,50), side='top', anchor='w')


        food_protein_texts.pack(pady=(10,10), side='top', anchor='w')
        self.food_protein_texts_entry.pack(padx= (0,90), side='top', anchor='w')

        button.pack(padx=20,pady=(30,10),side='top', anchor='w')
        
    def add_food_database(self):
        name = self.food_name_entry.get()
        unit = float(self.food_unit_entry.get())
        fat = float(self.food_fat_texts_entry.get())
        carbohydate = float(self.food_carbohydate_entry.get())
        protein = float(self.food_protein_texts_entry.get())

        self.data[name] = {
                "脂肪":fat/unit,
                "碳水":carbohydate/unit,
                "蛋白质":protein/unit,
        }

        with open("database.json", "w") as outfile:
            json.dump(self.data, outfile, ensure_ascii=False, indent=4)

        self.table.insert(parent='',index=tk.END, values=(name,
                                                          carbohydate/unit,
                                                          fat/unit,
                                                          protein/unit))