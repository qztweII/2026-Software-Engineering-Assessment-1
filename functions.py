import requests
import matplotlib

APILink = "https://fruityvice.com/api/fruit/"

def choices(list, query):
    for i in range(len(list)):
        print(f"[{i}] {list[i]}")
    while True:
        try:
            choice = int(input(query))
            list[choice]
        except ValueError:
            print("Please choose a number")
        except IndexError:
            print("Please choose an option within the above list")
        else:
            break
    return list[choice]
        

def fruitLookup(type):
    global APILink
    if type == "Name": 
        fruit = input("Search fruits: ")
        fruit_data = requests.get(f"{APILink}{fruit}")
    elif type == "Nutrition": 
        nutritions = ["Calories", "Fat", "Sugar", "Carbohydrates", "Protein"]
        nutrition = choices(nutritions)
        while True:
            try:
                min = int(input("Minimum amount of nutrition? "))
            except:
                print("Please choose a number")
            else:
                break
        while True:
            try:
                max = int(input("Maximum amount of nutrition? "))
            except:
                print("Please choose a number")
            else:
                break
        fruit_data = requests.get(f"{APILink}{nutrition}?min={min}&max={max}")
    if not "error" in fruit_data[0].keys(): 
        if len(fruit_data) > 1:
            names = []
            for i in requests:
                names.append(i["name"])
            fruit_chosen = choices(names, "Which fruit do you want to choose?")
            for i in range(len(fruit_data)):
                if fruit_data["name"] != fruit_chosen:
                    del fruit_data[i]
            fruit_data = fruit_data[0] #Turn fruit_data into dictionary from dictionary in list
    
    return fruit_data

def saveSearchHistory(thing):


def displayData(thing):


def addFruitsForCompare():


def compareFruits(list):
    

# def moreLikeThis(thing):


# def customiseGUI():


