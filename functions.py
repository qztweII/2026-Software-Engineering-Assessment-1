import requests
import numpy as np #I think matplotlib needs numpy
import matplotlib.pyplot as plt
import json

APILink = "https://fruityvice.com/api/fruit/"

def choices(list, query, numerical=False):
    '''Just makes inputs cleaner'''
    print()
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
        finally:
            print()
    if numerical:
        return choice
    else:
        return list[choice]
        
def saveSearchHistory(thing):
    '''Saving search history into a json file'''
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
    '''Loads the search history'''
    with open("history.json", "r") as f:
        history = json.load(f)
    
    return history

def fruitLookup(want, search=None):
    '''Look up fruits by name or filtering and choosing by nutritional value. Choose "Name" or "Nutrition". '''
    global APILink
    if want == "Name": 
        if search == None:
            fruit = input("Search fruits: ")
        else:
            fruit = search
        fruit_data = requests.get(f"{APILink}{fruit}")
        fruit_data = fruit_data.json()
        if not "error" in fruit_data:
            fruit_data = [fruit_data]
    elif want == "Nutrition": 
        nutritions = ["calories", "fat", "sugar", "carbohydrates", "protein"]
        if search == None:
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
        
        del fruit_data["family"]
        del fruit_data["order"]
        del fruit_data["genus"]

    return fruit_data




def displayData(thing):
    '''Prints fruit data nicer'''
    for i in thing:
        if i == "nutritions":
            for j in thing[i]:
                print(f"{j.capitalize()} : {thing[i][j]}")
        else:
            print(f"{i.capitalize()} : {thing[i]}")


def addFruitsForCompare(fruit=None):
    '''Function for user to add fruits to compare them. Deprecated'''
    list_of_fruits = []
    if fruit != None:
        list_of_fruits.append(fruit)
    using = True
    while using:
        fruit = fruitLookup(choices(["Name", "Nutrition"], "How do you want to search your next fruit? "))
        if not "error" in fruit:
            list_of_fruits.append(fruit)
            print(fruit["name"])
        else:
            print(f"Oh no! {fruit['error']}")
        if choices(["Yes", "No"], "Do you want to keep adding fruits for compare? ") == "No":
            using = False
    return list_of_fruits #This should return a list of dictionaries. 


def compareFruits(list):
    '''Graphs the fruits by nutritional value'''
    using = True
    while using:
        choice = choices(["Calories", "Fat", "Sugar", "Carbohydrates", "Protein", "Exit"], "What nutrition do you want to compare by? ").lower() #Capitalising here just makes the UI look prettier
        if choice == "exit":
            break
        nutrition = []
        for i in list:
            nutrition.append(i["nutritions"][choice])
        fruits = []
        for j in list:
            fruits.append(j["name"])

        #AAAAAAAAAA GRAPHING!!!!!! AAAAAAAAAAAA
        plt.bar(fruits, nutrition)
        plt.title(f"Fruits by {choice}")
        plt.xlabel("Fruits")
        plt.ylabel(choice)
        plt.show()
    

def exploreMore(thing):
    '''calls API for fruits of ±1 id'''
    print("Loading...")
    global APILink
    id = thing['id']
    more_like_this = []
    for i in range(-1, 2, 2):
        fruit = fruitLookup("Name", (id + i))
        if "error" in fruit:
            fruit = fruitLookup("Name", (id + i + i))
        more_like_this.append(fruit)
    return more_like_this



# def customiseGUI():
