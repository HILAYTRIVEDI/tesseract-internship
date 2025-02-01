def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = float(input("Enter a number: "))
print(f"The number is {check_number(number)}.")
