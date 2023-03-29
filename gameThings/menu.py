from inventory import items
from inventory import keyItems
from partyAttribs import partyMember1Attrib
from partyAttribs import partyMember2Attrib
from partyAttribs import partyMember3Attrib
from partyAttribs import partyMember4Attrib
from partyAttribs import partyMember5Attrib
import main

def menu():
    #assigning the very first choice
    choice = main.uiChoice()

    #menu ifs, controls menu choices as well as the end results.  
    if choice == "Menu" or choice == "M" or choice == "menu" or choice == "m":
        while True:
            print("           MENU             ")
            print("╔══════════════════════════╗")
            print("║          ITEM            ║")
            print("║          STATUS          ║")
            print("║          MAGIC           ║")
            print("║          SAVE            ║")
            print("║          QUIT            ║")
            print("║          EXIT            ║")
            print("╚══════════════════════════╝")
            
            
            print("Which option do you want?")
            choice = input("")
            
            if choice == "ITEM" or choice == "item" or choice == "I" or choice == "i":
                print(items)
                print("Do you want to use an item?")
                yesNo = input("")
                if yesNo == "YES" or yesNo == "Y" or yesNo == "yes" or yesNo == "y":
                    print("What item do you want to use?")
                    itemChoice = input("")
                    try:
                        items[itemChoice] = items[itemChoice] - 1
                        break
                    except ValueError:
                        print("You don't have enough of that item to use.")
                    except KeyError:
                        print("Item names are case sensitive. Make sure you spelled it correctly.")
                else:
                    continue
            elif choice == "STATUS" or choice == "status" or choice == "S" or choice == "s":
                print("Party Member 1")
                print("Party Member 2")
                print("Party Member 3")
                print("Party Member 4")
                print("Party Member 5")
                print("Whose stats are we checking?")
                choice = input("")
                if choice == 1:
                    print("pass")
                elif choice == 2:
                    print("pass")
                elif choice == 3:
                    print("pass")
                elif choice == 4:
                    print("pass")
                elif choice == 5:
                    print("pass")
                break
            elif choice == "MAGIC" or choice == "magic" or choice == "M" or choice == "m":
                print("Who should cast Magic?")
                print("Party Member 1")
                print("Party Member 2")
                print("Party Member 3")
                print("Party Member 4")
                print("Party Member 5")
                if choice == 1:
                    if partyMember1Attrib.Magic == 'yes':
                        print("pass")
                    else:
                        print("This party member cannot cast magic!")
                elif choice == 2:
                    if partyMember2Attrib.Magic == 'yes':
                        print("pass")
                    else:
                        print("This party member cannot cast magic!")
                elif choice == 3:
                    if partyMember3Attrib.Magic == 'yes':
                        print("pass")
                    else:
                        print("This party member cannot cast magic!")
                elif choice == 4:
                    if partyMember4Attrib.Magic == 'yes':
                        print("pass")
                    else:
                        print("This party member cannot cast magic!")
                elif choice == 5:
                    if partyMember5Attrib.Magic == 'yes':
                        print("pass")
                    else:
                        print("This party member cannot cast magic!")
                break
            elif choice == "SAVE" or choice == "save" or choice == "S" or choice == "s":
                while True:
                    try:
                        newSave = open("save.txt" , "x+")
                        newSave.write("pass")
                        print(newSave.read())
                        newSave.close()
                        break
                    except FileExistsError:
                        newSave = open("save.txt" , "w+")
                        print("Are you sure you wish to overwrite your save data?")
                        yesNo = input("")
                        if yesNo == "Yes" or yesNo == "yes" or yesNo == "y" or yesNo == "YES" or yesNo == "Y":
                            newSave.write("testicles")
                            print(newSave.read())
                        elif yesNo == "No" or yesNo == "NO" or yesNo == "no" or yesNo == "N" or yesNo == "n":
                            newSave.close()
                            choice = main.uiChoice()
                        else: 
                            print("Yes or no only please.")
                            continue
                        break
            elif choice == "QUIT" or choice == "quit" or choice == "Q" or choice == "q":
                print("Are you sure you want to quit?")
                choice = input("")
                if choice == "YES" or choice == "Y" or choice == "yes" or choice == "y":
                    print("")
                    break
                elif choice == "NO" or choice == "N" or choice == "no" or choice == "n":
                    choice = main.uiChoice()
                    break
            elif choice == "EXIT" or choice == "exit" or choice == "E" or choice == "e":
                print("pass")
                break