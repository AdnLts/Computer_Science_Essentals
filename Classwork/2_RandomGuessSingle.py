# Single Player Guessing Game
# This App allows a user to try to guess a random number

#----------------------------------------------------------------------------
# IMPORTS
import random
#----------------------------------------------------------------------------
# Variables
Player_Guess = -1
Random_Number= -1
Player_Lives = 5
Win = 0
#----------------------------------------------------------------------------
# GAME START
print("Hello! Welcome to the Single Player Guessing Game!")
print("Enter a number from 1-1000")
Random_Number = random.randint(1,1000)
#----------------------------------------------------------------------------
#IF GAME
while Player_Lives > 0:
    print(Player_Lives)
    Player_Guess = int(input("-> "))
    if Player_Guess == Random_Number:
        print("You Win!")
        Player_Lives = 0
        Win = 1
    elif Player_Guess > Random_Number:
        print("Guess Lower")
        Player_Lives -= 1
    elif Player_Guess < Random_Number:
        print("Guess Higher")
        Player_Lives -= 1
    else:
        print("ERROR   >:(")
        Player_Lives = 0
if Win != 1:
    print("YOU LOSE!")
