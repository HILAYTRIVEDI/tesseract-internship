# Program to check if a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

# Taking input from the user
try:
    num = int(input("Enter a number to check if it's even or odd: "))
    check_even_odd(num)
except ValueError:
    print("Invalid input! Please enter an integer.")
