def largest_of_three(a, b, c):
    return max(a, b, c)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print(f"The largest number is {largest_of_three(a, b, c)}.")
