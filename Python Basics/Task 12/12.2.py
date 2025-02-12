# Implement exception handling for invalid user input in a number conversion program.

def main():
    try:
        num = int(input("Enter a number: "))
        print("The number is", num)
    except ValueError:
        print("Invalid input. Please enter a number.")

main()
