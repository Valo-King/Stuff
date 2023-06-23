import random
secretWords = ["ascii" , "defenestrate" , "extraterrestrial" , "odin" , "gilgamesh" , "excalibur" , "risc" , "puffy" , "monstrous" , "monstrance" , "scapula" , "liturgical" , "cats" , "base" , "all your base"]
#this function handles game initialization
def initialize():
    while True:
        global guesses
        guesses = []
        global secretWord
        secretWord = random.choice(secretWords)
        global dashes
        dashes = ["-" for x in range(len(secretWord))]
        global handicap
        handicap = int(input("How many handicap guesses would you like this round? "))
        try: 
            handicap -= 1
            handicap += 1
            break
        except ValueError:
            print("Please enter a number.")
            continue
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
    print("Your number of guesses this time is: " + str(len(secretWord) + int(handicap)))
    for i in range(len(secretWord) + int(handicap) , -1 , -1):
        guess = getGuess()
#this continue statement goes up to the for loop, and takes away a guess. I think I can merge checkGuess and getGuess in some way, shape or form, but I'm not sure if it'll work the same way.
        if checkGuess(guess) == True:
            continue
        elif guess in secretWord:
            print("That letter is in the secret word!")
            updateDashes(guess)
        else:
            print("That letter is not in the secret word.")
        if "".join(dashes) in secretWord:
            print(secretWord + " was the secret word! Congration, you done it! :)")
            break
        print("You're getting signal: " + "".join(dashes))
        print("Your number of guesses remaining is: " + str(i))
        print("Do you think you know the deactivation key?")
        choice = input("")
        if choice.lower() == "yes" or choice.lower() == "y":
            superGuess = input("What you say??? ")
            if superGuess in secretWord:
                dashes.clear()
                for i in range(len(secretWord)):
                    dashes.append(secretWord[i])
                print(secretWord + " was the secret word! Smitty Alskephenbern Werbenmangensen smiles upon you!")
                break
            else:
                i = i - 1
                print("That was not it! You lose two guesses now!")
#when the for loop terminates without the player guessing the right word this should print the lose message.
    if "".join(dashes) != secretWord:
        print("Someone set up us the bomb. All your base.")
        print("in ur spaceship, bombin ur dudes")
        print("The secret word was: " + secretWord)
#This is a menu that lets the player decide if they would like to terminate the program or continue playing
    print("Play Again" , "Add Words" , "See Word List" , "Quit" , sep="\n")
    choice = input("What would you like to do? (match exact or acryonimize) ")
    if choice.lower() == "play again" or choice.lower() == "pa":
        pass
    elif choice.lower() == "add words" or choice.lower() == "aw":
        wta = input("What word would you like to add? ")
        secretWords.append(wta)
        choice = input("Would you like to see the word list? ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print("The word list is now: " + " ".join(secretWords))
    elif choice.lower() == "see word list" or choice.lower() == "swl":
        print(" ".join(secretWords))
    elif choice == "Quit" or choice == "Q" or choice == "q":
        break
