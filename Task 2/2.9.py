# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking user input
celsius_input = float(input("Enter temperature in Celsius: "))

# Converting and displaying the result
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")
