from functions import *
print("Welcome to FruitsApp!")
using = True
compare_list = []
wanna_compare = False #This is for the compare feature that is wired back to the search function. 
while using:
    mode = choices(["Search fruits", "Compare fruits", "Access History", "Exit"], "Please select:")
    
    if mode == "Search fruits":
        request = fruitLookup(choices(["Name", "Nutrition"], "How would you like to search fruits? By:"))
        if not 'error' in request:
            displayData(request)

            comparing = choices(["Yes", "No"], "Do you want to add to compare?")
            if comparing == "Yes":
                compare_list.append(request)
        else:
            print(f"Oh no! {request['error']}")
    
    elif mode == "Compare fruits":
        if len(compare_list) != 0:
            compareFruits(compare_list)
        else:
            print("You need to add fruits to compare")
            

    elif mode == "Access History":
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