# Write a program that handles division by zero using try-except.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter a valid number.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("Program executed successfully.")

