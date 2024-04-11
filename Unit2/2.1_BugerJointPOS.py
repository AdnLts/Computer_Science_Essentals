#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print("Use this kiosk to place your order")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Super Big Burger (5 Burgers) $10.24")
        print()
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK
        elif burgerChoice == "4":
            totalCost = totalCost+ 10.24
            print("You added Super Big Burger to your order")
            print("Your total cost so far: $", totalCost)

            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("sides")
        #Add your Code/Comments Here for sides
        #Add at least three sides
        print("We offer the following sides:")
        print("1: Fries $3.00")
        print()
        SideChoice = input("What would you like (input a number 1-1): ")
        #BURGER 1: HAMBURGER
        if SideChoice == "1":
            totalCost = totalCost + 3
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)
    elif menu == "Drinks":
        print("drinks")
        #Add Your code/Comments here for Drinks
        #Add at least three drinks
        print("We offer the following drinks:")
        print("1: Large Pepsi $4.50")
        print()
        DrinkChoice = input("What would you like (input a number 1-1): ")
        #BURGER 1: LPepsi
        if SideChoice == "1":
            totalCost = totalCost + 4.5
            print("You added a Large Pepsi to your order")
            print("Your total cost so far: $", totalCost)
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("order finished")
        print("You have ordered")
        print(burgerChoice,SideChoice,DrinkChoice)
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        print("Grand Total: $")
        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
