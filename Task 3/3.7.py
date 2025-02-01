# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI formula: weight (kg) / height (m)^2
    return bmi

# Function to interpret BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Taking input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Interpret BMI
category = interpret_bmi(bmi)

# Output the results
print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")
