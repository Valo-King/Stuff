import random
from inventory import items
from inventory import keyItems
#from partyAttribs import partyAttribs
from menu import menu

#updates keyItem dict (i.e. key items)
def updateKeyItems(newKeyItem , amnt):
    while True:
        if newKeyItem in keyItems:
            keyItems[newKeyItem] += amnt
            break
        else:
            keyItems[newKeyItem] = amnt
            break

#updates item dict (i.e. inv)
def updateItems(newItem , amnt):
    while True:
        if newItem in items:
            items[newItem] += amnt
            break
        else:
            items[newItem] = amnt
            break

def uiChoice():
    print("Where would you like to go?")
    return input("")

if uiChoice() == "MENU" or uiChoice() == "menu" or uiChoice() == "M" or uiChoice() == "m":
    menu()
elif uiChoice() == "7":
    updateItems("thirty" , 2)
    print(str(items))