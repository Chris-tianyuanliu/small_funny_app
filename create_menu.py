import json
import datetime
tdee = 2298
mass = 54
calorie = round(tdee*0.8, 1)
fat = round(calorie*0.25 / 9, 1)
protein = round(mass * 2.2, 1)
carbohydrates = round((calorie - protein * 4 - fat * 9)/4, 1)


# create the menu 
with open('menu.json', 'r') as openfile:

# Reading from json file
    menu = json.load(openfile)

date = str(datetime.date.today())
new_data = {
    date:{
        "剩余卡路里": calorie,
        "脂肪": fat,
        "碳水": carbohydrates,
        "蛋白质": protein,
        "早餐":{

        },
        "午餐":{

        },
        "晚餐":{

        },
    }
}


if menu == {}:
    menu = new_data
else:
    menu.update(new_data)

with open("menu.json", "w") as outfile:
    json.dump(menu, outfile, ensure_ascii=False, indent=4)