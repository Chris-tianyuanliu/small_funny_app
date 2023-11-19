from main_frame import MainFrame
from food_database import AddDatabase
from menu import AddMenu







if __name__ == "__main__":
    program = MainFrame()
    calorie, carbohydrates, fat, protein = program.return_initial_human_data()
    database = AddDatabase(program.window)
    menu = AddMenu(program.window, database.table, calorie, carbohydrates, fat, protein)
    program.window.mainloop()

















