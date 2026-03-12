import requests
#import matplotlib
import json

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
        
def saveSearchHistory(thing):
    with open("history.json", "r") as f:
        lines = f.read()
        if len(lines) == 0:
            first_thing = True
        else:
            first_thing = False

    lines = lines[1:-1]
    lines = (f"[{lines}{'' if first_thing else ','}{json.dumps(thing)}]")
    
    with open("history.json", "w") as f:
        f.write(lines)

def readSearchHistory():
    with open("history.json", "r") as f:
        history = json.loads(f)
    
    return history

def fruitLookup(want):
    global APILink
    if want == "Name": 
        fruit = input("Search fruits: ")
        fruit_data = requests.get(f"{APILink}{fruit}")
        fruit_data = fruit_data.json()
        if not "error" in fruit_data:
            fruit_data = [fruit_data]
    elif want == "Nutrition": 
        nutritions = ["calories", "fat", "sugar", "carbohydrates", "protein"]
        nutrition = choices(nutritions, "Choose nutrient: ")
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
        test = f"{APILink}{nutrition}?min={min}&max={max}"
        fruit_data = requests.get(test)
        fruit_data = fruit_data.json()
    if not "error" in fruit_data: 
        if len(fruit_data) > 1: #If a list of fruits come in
            names = []
            for i in fruit_data:
                names.append(i["name"])
            fruit_chosen = choices(names, "Which fruit do you want to choose?")
            for i in range(len(fruit_data)): #Get rid of everything that is not the fruit I want
                if fruit_data[i]["name"] != fruit_chosen:
                    fruit_data[i] = "None"
            fruit_data = [n for n in fruit_data if n != "None"] #Actually gets rid of it
        fruit_data = fruit_data[0] #Turn fruit_data into dictionary from dictionary in list
        if want == "Nutrition":
            saveSearchHistory({"type":"Nutrition", "nutrition":nutrition, "max": max, "min": min})
        else:
            saveSearchHistory({"type":"Name", "name":fruit})
        
        del fruit_data["id"]
        del fruit_data["family"]
        del fruit_data["order"]
        del fruit_data["genus"]

    return fruit_data




def displayData(thing):
    for i in thing:
        if i == "nutritions":
            for j in thing[i]:
                print(f"{j.capitalize()} : {thing[i][j]}")
        else:
            print(f"{i.capitalize()} : {thing[i]}")


def addFruitsForCompare():
    pass


def compareFruits(list):
    pass
    

# def moreLikeThis(thing):


# def customiseGUI():


if __name__ == "__main__":
    fruit = fruitLookup("Nutrition")
    if not "error" in fruit:
        displayData(fruit)