# Single Player Guessing Game
# This App allows a user to try to guess a random number

#----------------------------------------------------------------------------
# IMPORTS
import random
#----------------------------------------------------------------------------
# Variables
Player_Guess = -1
Random_Number= -1
Again = 1
#----------------------------------------------------------------------------
# GAME START
print("Hello! Welcome to the Single Player Guessing Game!")

while Again != 2:
    Random_Number = random.randint(1,1000)
    Player_Lives = 10
    Win = 0

    print("Enter a number from 1-1000")
    print()

    while Player_Lives > 0:
        try:
            print("Lives =", Player_Lives)
            Player_Guess = int(input("-> "))

            if Player_Guess == -7:
                print(Random_Number)

            elif Player_Guess == Random_Number:
                print("You Win!")
                Player_Lives = 0
                Win = 1

            elif Player_Guess > Random_Number:
                print("Guess Lower")
                print()
                Player_Lives -= 1

            elif Player_Guess < Random_Number:
                print("Guess Higher")
                print()
                Player_Lives -= 1

            else:
                print("ERROR   >:(")
                Player_Lives = 0
        except:
            print("An error has occured")
            print()
#---------------------------------------------------------------------------
#End Game
    if Win != 1:
        print("YOU LOSE!")
        print("The number was",Random_Number)
        print()
        print("Play Again?")
        print("Yes (1), No (2)")
        try:
            Again = int(input("-> "))

        except:
            print("An error has occured")
            break

    else:
        print()
        print("Play Again?")
        print("Yes (1), No (2)")
        try:
            Again = int(input("-> "))

        except:
            print("An error has occured")
            break

print("Thanks for playing!")
