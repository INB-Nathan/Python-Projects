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

def divideFunc():
    """Performs division with validation for non-zero denominator."""
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
            
    while True:
        try:
            denominator = int(input("Enter the denominator: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
    
    if denominator == 0:
        print("Error: Denominator cannot be zero.")
    try:
        result = numerator / denominator
        print("The quotient of {:} and {:} is: {:.2f}".format(numerator,denominator,result))
    except Exception as e:
        print(f"Error during division: {e}")

def exponentiationFunc():
    """Calculates base raised to the exponent with additional validation."""
    while True:
        try:
            base = int(input("Enter the base: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
            
    while True:
        try:
            exponent = int(input("Enter the exponent: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
    
    try:
        if exponent > 1000:
            print("Warning: Large exponent might cause overflow.")
        
        result = (base ** exponent)
        
        if abs(result) > 1e6:
            print(f"The exponentiation of {base} and {exponent} is: {result:e}")
        else:
            print(f"The exponentiation of {base} and {exponent} is: {result}")
    except Exception as e:
        print(f"Error during exponentiation: {e}")

def remainderFunc():
    """Finds remainder with validation for non-zero divisor."""
    while True:
        try:
            num = int(input("Enter the number: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
            
    while True:
        try:
            divisor = int(input("Enter the divisor: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
    
    if divisor == 0:
        print("Error: Divisor cannot be zero.")
    try:
        print(f"The divisor of {num} and {divisor} is: {num % divisor}")
    except Exception as e:
        print(f"Error during remainder calculation: {e}")

def summationFunc():
    """Sums numbers from start to end (inclusive) with improved range validation."""
    while True:
        try:
            start = int(input("Enter the start number: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
            
    while True:
        try:
            end = int(input("Enter the end number: "))
            break
        except ValueError:
            print("Invalid integer. Please enter a valid number.")
            continue
    
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
                func()
        else:
            print("\nInvalid choice. Please select a valid option.")
        
        input("\nPress Enter to continue...")

userMenu()
