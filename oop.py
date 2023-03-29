import math 
import random
colours = ["cornflower blue" , "yellow" , "red" , "blue"]
monsters = ["Zombie" , "Marlboro" , "Ghost" , "Frankstein's" , "Facehugger"]
killers = ["Gacy" , "Huntress" , "Unabomber"]


def takeFromList():
    while True:
        want = input("Do you want to take a selection? ")
        if want == "yes" or want == "Yes" or want == "Y" or want == "y":
            listToTakeFrom = input("What list do you want to take from? (colours, monsters, killers) ")
        elif want == "no" or want == "No" or want == "N" or want == "n":
            break
        else:
            print("Yes or no, dumbass.")
        try:
            if listToTakeFrom == "monsters":
                choice = random.choice(monsters)
                monsters.remove(choice)
                print(choice)
                continue
            elif listToTakeFrom == "colours":
                choice = random.choice(colours)
                colours.remove(choice)
                print(choice)
                continue
            elif listToTakeFrom == "killers":
                choice = random.choice(killers)
                killers.remove(choice)
                print(choice)
                continue
            else:
                print("That is not a valid list!")
                continue
        except IndexError:
            print("Oops! There's nothing left in that list. You won't be able to take another selection of that one without adding more to the list.")
            continue


def printMyLists():
    print("The content of the lists now looks like this:")
    print("Monsters: " + str(monsters))
    print("Killers: " + str(killers))
    print("Colours: " + str(colours))


while True:

    takeFromList()
    printMyLists()
    while True:
        want = input("Want to add to the lists? ")
        if want == "yes" or want == "Yes" or want == "Y" or want == "y":
            want = input("What list should we add to? (colours, killers, monsters) ")
            if want == "Killers" or want == "killers":
                want = input("What should we add? ")
                killers.append(want)
            elif want == "Colours" or want == "colours":
                want = input("What should we add? ")
                colours.append(want)
            elif want == "Monsters" or want == "monsters":
                want = input("What should we add? ")
                monsters.append(want)
            elif want == "" or want == " " or want == "  " or want == "   " or want == "    ":
                print("Why would I want to add nothing to my lists?")
                continue
            else:
                print("That is not a valid list!")
                continue
        
        elif want == "no" or want == "No" or want == "N" or want == "n":
            want2 = input("Do you still want to edit the lists? ")
            if want2 == "no" or want2 == "No" or want2 == "N" or want2 == "n":
                break
            elif want2 == "yes" or want2 == "Yes" or want2 == "Y" or want2 == "y":
                continue
            else:
                print("Yes or no, dumbass.")