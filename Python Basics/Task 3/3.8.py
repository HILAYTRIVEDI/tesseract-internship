# Function to calculate square and cube
def calculate_square_and_cube(number):
    square = number ** 2  # Square of the number
    cube = number ** 3    # Cube of the number
    return square, cube

# Taking input from the user
number = float(input("Enter a number: "))

# Calculate square and cube
square, cube = calculate_square_and_cube(number)

# Output the results
print(f"The square of {number} is {square}.")
print(f"The cube of {number} is {cube}.")
