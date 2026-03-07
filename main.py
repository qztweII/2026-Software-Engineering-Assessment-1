#Import all of the various script files
#BEGIN main.py
#using = True
#compare_list = []
#wanna_compare = False #This is for the compare feature that is wired back to the search function. 
#WHILE using
#   IF not wanna_compare:
#       type = Ask user for actions
#   ENDIF
#   IF type in ["Fruit Lookup", "Nutrition"] or wanna_compare:
#       search = Ask user for search term
#       IF search == "Back":
#           continue
#       ENDIF
#       request = fruitLookup(search)
#       IF request not has error:
#           saveSearchHistory
#           Print all of the data line by line
#
#           IF wanna_compare:
#               finished_comparing = Ask user if finished comparing
#               IF finished_comparing:
#                   compareFruits
#           ENDIF
#           ELSE:
#               comparing = Ask user if want to compare
#               IF comparing == "yes":
#                   wanna_compare = True
#               ENDIF
#           ENDELSE
#           
#       ENDIF
#       ELSE:
#           Show an error message
#       ENDELSE
#   ENDIF
#   ELIF type == "Exit":
#       using = False
#   ENDELIF
#ENDWHILE
#END main.py