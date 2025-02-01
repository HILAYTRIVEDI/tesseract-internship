# Function to check if a number is divisible by both 3 and 5
def is_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

# Taking input from the user
number = int(input("Enter a number: "))

# Check divisibility and print the result
if is_divisible_by_3_and_5(number):
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
