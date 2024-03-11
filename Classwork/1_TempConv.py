#Temperature Converter
#This program converts temperatures between Fahrenheit and Celcius

#It allow the user to specify if which way they want to convert
#The user then inputs their temperature
#And the converted number is printed to the terminal


print("Temperature Converter")
print("Which converstion would you like: (1) F to C, (2) C to F")
user_choice = input("->")

if user_choice == "1":
    print("Converting F to C")
    print("What is your number?")
    temp_input = input("->")
    #conversion: (F-32)*(5/9)
    temp_output = (float(temp_input)-32)*(5/9)
    print(temp_output," C")
elif user_choice == "2":
    print("Converting C to F")
    print("What is your number?")
    temp_input = input("->")
    #conversion: (C × 9/5) + 32 = F
    temp_output = (float(temp_input)*(5/9))+32
    print(temp_output," F")
else:
    print("Invalid Selection, please try again")
