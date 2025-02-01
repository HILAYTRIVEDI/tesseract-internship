# Function to check the type of a variable
def check_variable_type(variable):
    print(f"The value of the variable is: {variable}")
    print(f"The type of the variable is: {type(variable)}")

# Test cases with different variable types
int_var = 10
float_var = 10.5
string_var = "Hello, World!"
bool_var = True
list_var = [1, 2, 3, 4]
dict_var = {"name": "Alice", "age": 25}

# Checking types
check_variable_type(int_var)
check_variable_type(float_var)
check_variable_type(string_var)
check_variable_type(bool_var)
check_variable_type(list_var)
check_variable_type(dict_var)
