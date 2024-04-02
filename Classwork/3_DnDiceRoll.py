import random
#------------------------------
DiceNum = -1
Diceside = -1
Roll = 0
Total = 0
#------------------------------
print("Dice Roller")
try:
    DiceNum = int(input("Number of dice: "))
    print()
    Diceside = int(input("Number of sides on dice: "))
    print()
    while DiceNum > 0:
        Roll = random.randint(1,Diceside)
        print("Roll ",DiceNum," is ",Roll)
        DiceNum -= 1
        Total += Roll
    print("The total is ",Total)
except:
    print("an error has occured")
