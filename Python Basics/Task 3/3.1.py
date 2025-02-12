# Simple Calculator Program

def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of addition: {num1 + num2}")
        elif choice == '2':
            print(f"The result of subtraction: {num1 - num2}")
        elif choice == '3':
            print(f"The result of multiplication: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of division: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            print(f"The result of modulus: {num1 % num2}")
        elif choice == '6':
            print(f"The result of exponentiation: {num1 ** num2}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
