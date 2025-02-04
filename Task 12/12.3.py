# Create a function that raises a ValueError if a negative number is passed.

def raise_value_error(n):
    try:
        if n < 0:
            raise ValueError("Negative number passed")
        
        return n
    except ValueError as e:
        return e
    

value = input("Enter a number: ")
print(raise_value_error(value))