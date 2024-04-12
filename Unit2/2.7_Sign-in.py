FileName = "SignIn.txt"
#--------------------------------------------------------------
# Methods

# Write
def writeToFile(Name):
    try:
        with open(FileName, 'a') as file:
            Name = Name +"\n"
            file.write(Name)
            print("Hello ",Name)
            print("Succesfully Signed in!")
            print()
            file.close()
    except:
        print("An error has occured!")

#Read
def readFromFile():
    try:
        with open(FileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occured!")
#-----------------------------------------------------------------
# Loop

# Start
while True:
    print("What would you like to do?")
    print("1: Sign-in   2:Read sign-in list   3:exit program")
    choice = input("->")
    if choice == "1":
        print("Please enter your name")
        Name = input("->")
        writeToFile(Name)

    elif choice == "2":
        print("Reading Sign-in")
        readFromFile()

    elif choice == "3":
        break
print("Good Bye")
