#By C0d3M@th
#Made Fri 1/28/22

operation = "Hamburger"
goodoper = False
opernumber = 909090909
number1 = 0
number2 = 0
result = 0
print("This is a simple calculator. It does +-*/ only.")
print("")
while goodoper == False:
    print("Please type the number corresponding to your operation. 1=+,2=-,3=*,4=/")
    opernumber = int(input())
    if opernumber not in [1,2,3,4]:
        print("I didn't understand that. Please try again.")
    else:
        goodoper = True
        if opernumber == 1:
            print("You have selected addition.")
            operation = "Addition"
        if opernumber == 2:
            print("You have selected subtraction.")
            operation = "Subtraction"
        if opernumber == 3:
            print("You have selected multiplication.")
            operation = "Multiplication"
        if opernumber == 4:
            print("You have selected division.")
            operation = "Division"
print("")
print("What is your first number?")
number1 = int(input())
print("What is your second number?")
number2 = int(input())
print("")
if operation == "Addition":
    result = number1 + number2
elif operation == "Subtraction":
    result = number1 - number2
elif operation == "Multiplication":
    result = number1 * number2
else:
    result = number1/number2
print("Your result is " + str(result) + ".")
print("Thanks for using this four function calculator!")