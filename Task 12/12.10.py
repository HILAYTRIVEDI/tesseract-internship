def process_numbers(a, b):
    try:
        print("Starting the process...")

        try:
            # First, try dividing the numbers
            result = a / b
            print(f"Division result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")

        try:
            # Now, try converting the result to an integer
            int_result = int(result)
            print(f"Converted result to integer: {int_result}")
        except NameError:
            print("Error: Division failed, so no result to convert!")
        except ValueError:
            print("Error: Cannot convert result to integer!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Process completed.\n")

# Test cases
process_numbers(10, 2)    # Normal case
process_numbers(5, 0)     # Division by zero
process_numbers('five', 2)  # Invalid input type
