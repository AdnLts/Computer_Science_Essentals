import random
#------------------------------
DiceNum = -1
Diceside = -1
Roll = 0
#------------------------------
print("Dice Roller")
DiceNum = int(input("Number of dice: "))
print()
Diceside = int(input("Number of sides on dice: "))
print()
#------------------------------
while DiceNum > 0:
  Roll = random.randint(1,Diceside)
  print("Roll "+str(DiceNum)+" is "+str(Roll))
  DiceNum -= 1
