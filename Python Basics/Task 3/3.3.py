# Program to compare two numbers

def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

# Taking input from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    compare_numbers(number1, number2)
except ValueError:
    print("Invalid input! Please enter numeric values.")
