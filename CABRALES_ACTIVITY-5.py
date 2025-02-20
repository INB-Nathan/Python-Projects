# Nathan Josua C. Cabrales
# 202312375
# TC22
# 02/20/2025

# (❁´◡`❁)

# Laboratory Activity: Function
# Create a program that will simulate the following mathematical operations. 
# Design a menu that will ask the user to enter the choice and provide each functions for each operations. 
# The functions must provide the following validation on each given input. A None value must be return.
# [D] - Divide (the second number or denominator must not be equal to zero)
# [E] - Exponentiation
# [R] - Remainder (the second number or denominator must not be equal to zero)
# [F] - Summation (the two numbers are the limits and it must be the second number must be greater than the first number, if the input is 4 and 8 the sum must be 4 + 5 + 6 + 7 + 8).

def userMenu():
    ''' This is the user menu that will be displaying when the program is first run, and will be looped upon completion of a function. '''
    choice = "X"
    while choice != "D" or choice != "E" or choice != "R" or choice != "F" or choice != "G":
        print(("=" * 20) +" USER MENU " + ("=" * 20))
        print("%0s %5s" % ("[D].","Divide"))
        print("%0s %5s" % ("[E].","Exponentiation"))
        print("%0s %5s" % ("[R].","Remainder"))
        print("%0s %5s" % ("[F].","Summation"))
        print("%0s %5s" % ("[G].","Exit"))
        print("=" * 51)
        choice = input("Enter the function to be used: ")
        choice.upper()
        if choice != "D" or choice != "E" or choice != "R" or choice != "F" or choice != "G":
            input("You did not input a valid key, press a key to return...") 
    if choice == "G":
        print("Exiting the program...")
    elif choice == "D":
        divideFunc()
    elif choice == "E":
        exponentiationFunc()
    elif choice == "R":
        remainderFunc()
    elif choice == "F":
        summationFunc()

    
        
def divideFunc(userChoice):
    ''' This function will divide the second number or denominator must not be equal to zero '''
    try:
        firstNum = int(input("Enter the first number or numerator: "))
        secondNum = int(input("Enter the second number or numerator: "))
    except :

    finally:
        


def exponentiationFunc(userChoice):
    ''' This function will exponentiatiate the user value to the asked value. '''

def remainderFunc(userChoice):
    ''' This function will take two numbers and get the remainder. The second number or denominator must not be equal to zero '''

def summationFunc(userChoice):
    ''' This function will get the range of two numbers and plus each value in that range. the two numbers are the limits and it must be the second number must be greater than the first number, if the input is 4 and 8 the sum must be 4 + 5 + 6 + 7 + 8  '''


userMenu()
