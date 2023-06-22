#a list of all letters in the english language
letters = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

#this function takes a message that must be encrypted, lowerizes it, and returns it to be assigned to a variable.
def messageIn():
    message = input("What would you like to shift? ")
    return message.lower()

messageHair = []
for letter in messageIn():
    messageHair.append(letter)

shift = int(input("How many would you like to shift by? "))

for i in range(len(messageHair)):
    messageHair[i] = letters[i+shift] 
print("".join(messageHair))
