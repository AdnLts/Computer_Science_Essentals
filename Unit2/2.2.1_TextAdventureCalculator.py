#Text Adventure Calculator
#The only calculator with a chance to not work

import random

answerList = []

#functions

# Addition Function
# Adds two user supplied number
def Add(fail):
    print("This calculator takes two user supplied numbers and adds them together.")
    try:
        NUM1=float(input("Enter the first number: "))
        NUM2=float(input("Enter the Second number: "))
        # If It wont fail:
        if fail != 3:
            Answer=NUM1+NUM2
            print()
            print("The Answer is ",Answer) 
        # If it will fail:
        else:
            Answer = random.randint(0,1000000)
            print()
            print("The Answer is ",Answer)            
        answerList.append(Answer)
    #Crash Prevent
    except:
        print("An Error Has Occured")
    return
    
# Subtraction Function
# Suvbstracts two user supplied numbers
def Sub(fail):
    print("This calculator takes two user supplied numbers and subtracts them.")
    try:
        NUM1=float(input("Enter the first number: "))
        NUM2=float(input("Enter the Second number: "))
        # If It wont fail:
        if fail != 3:
            Answer=NUM1-NUM2
            print()
            print("The Answer is ",Answer) 
        # If it will fail:
        else:
            Answer = random.randint(0,1000000)
            print()
            print("The Answer is ",Answer)             
        answerList.append(Answer)
    #Crash Prevent
    except:
        print("An Error Has Occured")
    return

# Multiply Function
# Multiplies two user supplied numbers
def Mult(fail):
    print("This calculator takes two user supplied numbers and multiplies them.")
    try:
        NUM1=float(input("Enter the first number: "))
        NUM2=float(input("Enter the Second number: "))
        # If It wont fail:
        if fail != 3:
            Answer=NUM1*NUM2
            print()
            print("The Answer is ",Answer) 
        # If it will fail:
        else:
            Answer = random.randint(0,1000000)
            print()
            print("The Answer is ",Answer)             
        answerList.append(Answer)
    #Crash Prevent
    except:
        print("An Error Has Occured")
    return

# Division Calculator
# Divides two user supplied numbers
def Div(fail):
    print("This calculator takes two user supplied numbers and divides them.")
    try:
        NUM1=float(input("Enter the first number: "))
        NUM2=float(input("Enter the Second number: "))
        # If It wont fail:
        if fail != 3:
            Answer=NUM1/NUM2
            print()
            print("The Answer is ",Answer) 
        # If it will fail:
        else:
            Answer = random.randint(0,1000000)
            print()
            print("The Answer is ",Answer)             
        answerList.append(Answer)
    #Crash Prevent
    except:
        print("An Error Has Occured")
    return


#FailChance
#Gives Chance to fail
# Anything but 3 will give the right answer
FailChance = random.randint(0,6)


#Start
print("Welcome to the Text Adventure Calculator")
while True:
    print()
    print("Would you like to:")
    print()
    print("(1) Add")
    print("(2) Subtract")
    print("(3) Multiply")
    print("(4) Divide")
    print("(5) Look at previous answers")
    print("(6) Exit Program")

    choose = input("-> ")
    print()

    if choose == "1":
        #Call Add
        Add(FailChance)

    elif choose == "2":
        #Call Subtract
        Sub(FailChance)
    
    elif choose == "3":
        #Call Multiply
        Mult(FailChance)

    elif choose == "4":
        #Call Divide
        Div(FailChance)

    elif choose == "5":
        #Print Answer List
        print("Previous Answers: ", answerList)

    elif choose == "6":
        #End Loop
        break

    else:
        #Error response
        print("Please select a valid option")
        print()
