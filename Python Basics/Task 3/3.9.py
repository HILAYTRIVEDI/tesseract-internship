# Function to calculate the remainder of division
def calculate_remainder(dividend, divisor):
    remainder = dividend % divisor  # Remainder using modulus operator
    return remainder

# Taking input from the user
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Calculate remainder
remainder = calculate_remainder(dividend, divisor)

# Output the result
print(f"The remainder when {dividend} is divided by {divisor} is {remainder}.")
