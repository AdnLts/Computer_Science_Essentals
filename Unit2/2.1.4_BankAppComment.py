#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)
#Withdraw
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    #Deposit
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    #check balance
    def CheckBal(self):
        return self.balance

#Code Start
print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)

#Creates Loop until user enters sign out
looper = 0
while looper == 0:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance   (4) Sign Out")
    choice = input("->")

    #Withdraw
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("You have $", customer.balance)
        print()
    #deposit
    elif choice == "2":
        print("How much are you depositing")
        amount = float(input("->"))
        customer.deposit(amount)
        print("You have deposited ", amount)
        print("You have $", customer.balance)
        print()
    #Add the ability to check balance
    elif choice == "3":
        print("You have $", customer.balance)
        print()

    #End
    elif choice == "4":
        looper = 1
        print("Thank you for banking with us.")
    #Invalid Option
    else:
        print("Please enter a valid option")
        print()
