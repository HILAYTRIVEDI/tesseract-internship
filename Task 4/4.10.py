import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif not re.search("[a-z]", password):
        return "Weak"
    elif not re.search("[A-Z]", password):
        return "Weak"
    elif not re.search("[0-9]", password):
        return "Weak"
    else:
        return "Strong"

password = input("Enter your password: ")
print(f"Password strength: {check_password_strength(password)}")
