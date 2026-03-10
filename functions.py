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
        

def fruitLookup(want):
    global APILink
    if want == "Name": 
        fruit = input("Search fruits: ")
        fruit_data = requests.get(f"{APILink}{fruit}")
        fruit_data = fruit_data.json()
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
        test = f"{APILink}{nutrition}?min={min}&max={max}" #DEBUGGING
        print(test)
        fruit_data = requests.get(test)
        fruit_data = fruit_data.json()
        print(fruit_data)
        if not type(fruit_data) == "dict": #Errors come as a dict
            if len(fruit_data) > 1:
                names = []
                for i in fruit_data:
                    names.append(i["name"])
                fruit_chosen = choices(names, "Which fruit do you want to choose?")
                for i in range(len(fruit_data)): #Get rid of everything that is not the fruit I want
                    if fruit_data[i]["name"] != fruit_chosen:
                        fruit_data[i] = "None"
                fruit_data = [n for n in fruit_data if n != "None"] #Actually gets rid of it
            fruit_data = fruit_data[0] #Turn fruit_data into dictionary from dictionary in list
    return fruit_data

def saveSearchHistory(thing):
    pass


def displayData(thing):
    pass


def addFruitsForCompare():
    pass


def compareFruits(list):
    pass
    

# def moreLikeThis(thing):


# def customiseGUI():


if __name__ == "__main__":
    print(fruitLookup("Nutrition"))