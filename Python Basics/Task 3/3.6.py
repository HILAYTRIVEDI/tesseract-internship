import math

# Function to calculate the area of a circle
def calculate_area(radius):
    area = math.pi * radius ** 2  # Formula for the area of a circle
    return area

# Taking input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and print the area
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
