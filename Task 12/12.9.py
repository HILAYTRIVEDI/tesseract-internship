import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError as e:
        print("Error: You can't divide by zero!")
        logging.error(f"ZeroDivisionError: {e}")
    except TypeError as e:
        print("Error: Invalid input type!")
        logging.error(f"TypeError: {e}")
    finally:
        print("Division attempt finished.\n")

# Test cases
divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers('five', 2)
