import requests
import numpy as np #I think matplotlib needs numpy
import matplotlib.pyplot as plt
import json

APILink = "https://fruityvice.com/api/fruit/"

def choices(list, query, numerical=False, help=False):
    '''Just makes inputs cleaner, now with a help function'''
    print()
    while True:
        try:
            print(query)
            for i in range(1, (len(list) + 1)): #List out all the choices
                print(f"[{i}] {list[i-1]}")
            if not help == False: #List the help function
                print(f"[{i + 1}] Help me!!!")
            choice = int(input("Please choose a number: ")) #The actual asking
            if choice == (i+1): #Help function is always the last choice
                helpMe(help) 
            list[choice-1] #Otherwise check if the choice is in the list
        except ValueError:
            print("Please choose a number")
        except IndexError:
            if choice != (i+1): #If help is not selected
                #I did this instead of putting an else before line 20 because I want the function to loop back after the user used the help function
                print("Please choose an option within the above list")
        else:
            break
        finally:
            print()
    if numerical:
        return choice
    else:
        return list[choice-1]
        
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
    #Writing the json file, still as a single line

    with open("history.json", "w") as f:
        f.write(lines) #Actually writing to the file

def readSearchHistory():
    '''Loads the search history'''
    with open("history.json", "r") as f:
        history = json.load(f)
    
    return history

def fruitLookup(want, search=None, save=True):
    '''Look up fruits by name or filtering and choosing by nutritional value. Choose "Name" or "Nutrition" for want. '''
    global APILink
    if want == "Name": 
        if search == None:
            fruit = input("Search fruits: ")
            if len(fruit) == 0: #Empty requests default to pitahaya (dragonfruit)
                fruit = "pitahaya"
        else:
            fruit = search
        fruit_data = requests.get(f"{APILink}{fruit}") #Line that actually gets the data
        fruit_data = fruit_data.json()
        if not "error" in fruit_data: #API returns multiple fruits as a list or dictionary, but errors are always dictionaries
            fruit_data = [fruit_data] #All errors are dictionaries and all fruit data are in lists
    elif want == "Nutrition": 
        nutritions = ["calories", "fat", "sugar", "carbohydrates", "protein"] #Nutritions are hard-coded here
        if search == None:
            nutrition = choices(nutritions, "Choose nutrient: ", help="searchChoose")
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
        fruit_data = fruit_data.json() #Turn to json
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
        if save:
            if want == "Nutrition":
                saveSearchHistory({"type":"Nutrition", "nutrition":nutrition, "max": max, "min": min})
            else:
                saveSearchHistory({"type":"Name", "name":fruit})
        
        #Remove stuff I don't need
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


def compareFruits(list):
    '''Graphs the fruits by nutritional value'''
    using = True
    while using:
        choice = choices(["Calories", "Fat", "Sugar", "Carbohydrates", "Protein", "Exit"], "What nutrition do you want to compare by? ", help="graph").lower() #Capitalising here just makes the UI look prettier
        if choice == "exit":
            break
        nutrition = []
        for i in list:
            nutrition.append(i["nutritions"][choice])
        fruits = []
        for j in list:
            fruits.append(j["name"])

        #Graphing part
        plt.bar(fruits, nutrition)
        plt.title(f"Fruits by {choice}")
        plt.xlabel("Fruits")
        plt.ylabel(choice)
        plt.show()
    

def exploreMore(thing):
    '''calls API for fruits of ±1 id'''
    global APILink
    id = thing['id']
    more_like_this = []
    for i in range(-1, 2, 2):
        dontSave = False
        fruit = fruitLookup("Name", (id + i), False)
        j = 1
        while "error" in fruit:
            j += 1
            fruit = fruitLookup("Name", (id + (i * j)), False)
            if j == 4:
                dontSave = True
                break
        if not dontSave:
            more_like_this.append(fruit)
    return more_like_this

def helpMe(place):
    '''Display help at different places'''
    f = open("help.json")
    helpText = json.load(f) #edit help strings at help.json
    print(helpText[place])

# def customiseGUI():
