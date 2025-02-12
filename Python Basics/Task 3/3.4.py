# Program to check if a number is between 10 and 50

def check_number_range(num):
    if num > 10 and num < 50:
        print(f"{num} is between 10 and 50.")
    else:
        print(f"{num} is not between 10 and 50.")

# Taking input from the user
try:
    number = float(input("Enter a number: "))
    check_number_range(number)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
