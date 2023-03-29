#intializing
eggsMin = 1
flourMin = 100
milkMin = 200
print("Hello comrade!")
print("Blinmaker is starting for you!")
print("...")
print("...")
print("...")
userName = input("What is your name, comrade? ")
print("Greetings, Comrade " + userName + "!")

#taking aount of blin ingredient
eggsAmount = int(input("How many eggs you have, " + userName + "?"))
flourAmount = int(input("How much flour you have, " + userName + "?(Grams, please)"))
milkAmount = int(input("How much milk you have, " + userName + "?(Mililiter, comrade.)"))

#checking if we can make any blins
if eggsAmount < eggsMin or flourAmount < flourMin or milkAmount < milkMin:
    print("You don't have enough to make any blins, блять! How close are you to end of month, comrade?")
print("You have " + str(eggsAmount) + " eggs, " + str(flourAmount) + "g flour, and " + str(milkAmount) + "ml milk. If this is not correct, please restart the program.")

# math
eggsAmount = eggsAmount / eggsMin
flourAmount = flourAmount / flourMin
milkAmount = milkAmount / milkMin

#figuring out how many blins we can actually make
print("You have " + str(eggsAmount) + " portions of eggs, " + str(flourAmount) + " portions of flour, and " + str(milkAmount) + " portions of milk.")
if(eggsAmount > flourAmount) and (eggsAmount > milkAmount):
    print("You can make " + str(eggsAmount) + " blin(s)!")
    print("Blinmaker is shutting down...")
    print("Goodbye, Comrade " + userName + "!")
elif(flourAmount > eggsAmount) and (flourAmount > milkAmount):
    print("You can make " + str(flourAmount) + " blin(s)!")
    print("Blinmaker is shutting down...")
    print("Goodbye, Comrade " + userName + "!")
else:
    print("You can make " + str(milkAmount) + " blin(s)!")
    print("Blinmaker is shutting down...")
    print("Goodbye, Comrade " + userName + "!")