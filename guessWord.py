import random , sys
secretWords = ["ascii" , "defenestrate" , "extraterrestrial" , "odin" , "gilgamesh" , "excalibur" , "risc" , "puffy"
"monstrous" , "monstrance" , "scapula" , "liturgical" , "cats" , "base" , "all your base"]
#this function handles game initialization
def initialize():
    global guesses
    guesses = []
    global secretWord
    secretWord = random.choice(secretWords)
    global dashes
    dashes = ["-"] * len(secretWord)
#this function updates our secret word check, dashes, to carry the new letter
def updateDashes(guess):
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            dashes[i] = guess
#this function gets the guess and checks it against our parameters, then returns it if there isn't a problem
def getGuess():
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Your guess must be a single letter.")
            continue
        elif len(guess) == 1 and bool(guess.islower) == True:
            break
        else:
            print("Unexpected error.")
            continue
    return guess
def checkGuess(guess):
    if guess in guesses:
        print("Don't guess the same letter twice!")
        return True
    else:
        guesses.append(guess)
#this while loop is a sort of runtime for the game, and is terminates when playAgain is equal
#to something other than an emphatic yes. the for loop should be an amount of loops equal to the length of
#the secret word + 5, or some other arbitrary number. I would like to add code that allows 
#a user to guess the full word if they think they know what it is, and to add words to the 
#list of secret words in memory.
print("We've got bomb on the ship! Figure out the voice deactivation key, we only have so long!")
while True:
    initialize()
    for i in range(len(secretWord) + 5 , 0 , -1):
        guess = getGuess()
        if checkGuess(guess) == True:
            continue
        elif guess in secretWord:
            print("That letter is in the secret word!")
            updateDashes(guess)
        else:
            print("That letter is not in the secret word.")
        print("You're getting signal: " + "".join(dashes))
        print("Your number of guesses remaining is: " + str(i))
        if "".join(dashes) in secretWord:
            print(secretWord + " was the secret word! Congration, you done it! :)")
            break
#when the for loop terminates without the player guessing the right word this should print the lose message.
    if "".join(dashes) != secretWord:
        print("Someone set up us the bomb. All your base.")
        print("in ur spaceship, bombin ur dudes")
        print("The secret word was: " + secretWord)
#This is a menu that lets the player decide if they would like to terminate the program or continue playing.
    while True:
        print("Play Again" , "Add Words" , "See Word List" , "Quit" , sep="\n")
        choice = input("What would you like to do? (match exact or acryonimize) ")
        if choice == "Play Again" or choice == "PA" or choice == "pa":
           continue
        elif choice == "Add Words" or choice == "AW" or choice == "aw":
            wta == input("What word would you like to add? ")
            secretWords.append(wta)
            print("The word list is now: " + " ".join(secretWords))
        elif choice == "See Word List" or choice == "SWL" or choice =="swl":
            print(" ".join(secretWords))
        elif choice == "Quit" or choice == "Q" or choice == "q":
            sys.exit()
