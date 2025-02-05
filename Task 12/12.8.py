def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    else:
        print(f"Success! The result of {a} divided by {b} is {result}")
    finally:
        print("Division attempt finished.\n")

divide_numbers(10, 2)
divide_numbers(5, 0)
