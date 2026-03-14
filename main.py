from functions import *
print("Welcome to FruitsApp!")
using = True
compare_list = []
wanna_compare = False #This is for the compare feature that is wired back to the search function. 
while using:
    mode = choices(["Search fruits", "Access History", "Exit"], "Please select:")
    if mode in "Search fruits":

        request = fruitLookup(choices(["Name", "Nutrition"], "How would you like to search fruits? By:"))
        if not 'error' in request:
            displayData(request)

            comparing = choices(["Yes", "No"], "Do you want to add to compare?")
            if comparing == "yes":
                compare_list.append(addFruitsForCompare())
                compareFruits(compare_list)
                compare_list = [] #Reset the compare list
        else:
            print(f"Oh no! {mode['error']}")

    if mode == "Access History":
        history = readSearchHistory()
        history_nice = []
        for i in history:
            if i["type"] == "Name":
                history_nice.append(i['name'])
            else:
                history_nice.append(f"{i['nutrition']} ({i['min']} - {i['max']})")
        
        for i in history_nice: #I'm not bothered to give fruitLookup an automated method (yet)
            print(i)   
 
    elif mode == "Exit":
        using = False