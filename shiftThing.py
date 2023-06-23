#a list of all letters in the english language
#i absolutely cannot stand the way this is done but
#i don't know enough about python to do it better.
letterList = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" , "a" , "b" , "c" , "d" , "e" , "f" , "h" ,"i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w", "x" , "y" , "z" , "a" , "b" , "c" , "d" , "e" , "f" , "g" "h" , "i"]

#this function takes a message that must be encrypted, lowerizes it, and returns it to be assigned to a variable.
def messageIn():
    message = input("What would you like to shift? ")
    return message.lower()
#list comprehension fuckery that does the for loop stuff in a single line, cause that's cooler
messageHair = [letter for letter in messageIn()]

#taking the number to shift by and making sure it won't cause problems
while True:
    try:
        shift = int(input("How many would you like to shift by? ")) 
        if shift >= 26:
            print("\nless than 26, please.")
            continue
        else:
            break
    except ValueError:
        print("\nYou must enter a number.")
        continue
#this for-loop evaluates messageHair to see if the letter at i occurs in 
#letterList, then gets the index of that occurance,
#replaces the letter at i with the letter at that index+the shift number.
for i in range(len(messageHair)):
    if messageHair[i] in letterList:
        index = letterList.index(messageHair[i])
        messageHair[i] = letterList[index+shift]


print("".join(messageHair))
