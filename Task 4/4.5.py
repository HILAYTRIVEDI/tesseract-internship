def login_system(username, password):
    correct_username = "user123"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Login failed. Incorrect username or password."

username = input("Enter username: ")
password = input("Enter password: ")

print(login_system(username, password))
