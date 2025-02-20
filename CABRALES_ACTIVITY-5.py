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

def getInteger(prompt):
    """Optimized get integer so that i don't need to duplicate variableName = int(input("string"))"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue

def divideFunc():
    """Performs division with validation for non-zero denominator."""
    numerator = getInteger("Enter the numerator: ")
    denominator = getInteger("Enter the denominator: ")
    
    if denominator == 0:
        print("Error: Denominator cannot be zero.")
    try:
        result = numerator / denominator
        print("The quotient of {:} and {:} is: {:.2f}".format(numerator,denominator,result))
    except Exception as e:
        print(f"Error during division: {e}")

def exponentiationFunc():
    """Calculates base raised to the exponent with additional validation."""
    base = getInteger("Enter the base: ")
    exponent = getInteger("Enter the exponent: ")
    
    try:
        result = base ** exponent
        print(f"The exponentiation of {base} and {exponent} is: {result}")
    except Exception as e:
        print(f"Error during exponentiation: {e}")

def remainderFunc():
    """Finds remainder with validation for non-zero divisor."""
    num = getInteger("Enter the number: ")
    divisor = getInteger("Enter the divisor: ")
    
    if divisor == 0:
        print("Error: Divisor cannot be zero.")
    try:
        print(f"The divisor of {num} and {divisor} is: {num % divisor}")
    except Exception as e:
        print(f"Error during remainder calculation: {e}")

def summationFunc():
    """Sums numbers from start to end (inclusive) with improved range validation."""
    start = getInteger("Enter the start number: ")
    end = getInteger("Enter the end number: ")
    
    if end < start:
        print("Error: End must be greater than or equal to start.")
    try:
        n = end - start + 1
        total = n * (start + end) // 2
        print(f"The summation of {start} and {end} is: {total}")
    except Exception as e:
        print(f"Error during summation: {e}")

def userMenu():
    """Displays menu and handles user choices with improved validation and formatting."""
    menu_options = {
        'D': ('Divide', divideFunc),
        'E': ('Exponentiation', exponentiationFunc),
        'R': ('Remainder', remainderFunc),
        'F': ('Summation', summationFunc),
        'G': ('Exit', None)
    }
    
    while True:
        print("\n" + "=" * 20 + " USER MENU " + "=" * 20)
        for key in ['D', 'E', 'R', 'F', 'G']:
            print(f"[{key}] {menu_options[key][0]}")
        print("=" * 51)
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'G':
            print("Exiting the program. Goodbye!")
            break
        if choice in menu_options:
            func = menu_options[choice][1]
            if func:
                result = func()
                if result is not None:
                    print(f"\nResult: {result}")
        else:
            print("\nInvalid choice. Please select a valid option.")
        
        input("\nPress Enter to continue...")

userMenu()
