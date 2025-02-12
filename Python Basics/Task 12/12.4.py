# Implement a program to handle file-not-found errors.

try:
    file = open("file.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")
