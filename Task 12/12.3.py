def check_positive_number(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed!")
    else:
        print(f"The number {number} is valid.")



value = int(input("Enter a number: "))