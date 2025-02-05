# Implement a try-finally block to ensure file closure after reading.

try:
    file = open("file.txt", "r")
    print(file.read())

finally:
    file.close()
