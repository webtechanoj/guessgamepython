# Guess game
import random

guessNumber = (random.randint(1,50))

playerName = input("Hey Player, what's your name: ")
print ("Hello, "+ playerName + ", I am thinking of a number between 1 and 20")
print("Take a guess.")
i = 0
print(guessNumber)
while i<=5:
    i += 1
    guess = int(input())
    if guess > guessNumber:
        print("Your choice is high, you have "+ str(5-i) + " attempts")

    elif guess < guessNumber:
        print("Your choice is low, you have "+ str(5-i) + " attempts")

    else:
        print ("Bravooooooo!!! You guessed it in  " + str(i) + " attempt" )
        break



