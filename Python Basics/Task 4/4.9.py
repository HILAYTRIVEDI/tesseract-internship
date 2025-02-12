def categorize_number(number):
    if number < 10:
        return "Small"
    elif number < 100:
        return "Medium"
    else:
        return "Large"

number = float(input("Enter a number: "))
print(f"The number is categorized as {categorize_number(number)}.")
