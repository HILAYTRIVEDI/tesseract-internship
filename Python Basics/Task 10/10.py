# 1. Read a text file and print its contents
with open("test.txt" , 'r' ) as file:
    content = file.read()
    print(content)


# 2. Write user input into a file
with open("test.txt" , 'w' ) as file:
    file.write(input("Enter the text you want to write in the file: "))

# 3. Append data to an existing file
with open("test.txt" , 'a' ) as file:
    file.write(input("Enter the text you want to append in the file: "))

# 4. Count the number of words in a file
with open("test.txt" , 'r' ) as file:
    content = file.read()
    words = content.split()
    print("Number of words in the file are: ", len(words))

# 5. Copy the contents of one file to another
with open("test.txt" , 'r' ) as file:
    content = file.read()
    with open("test2.txt" , 'w' ) as file2:
        file2.write(content)
        
# 6. Read a CSV file and print its contents
import csv

with open("test.csv" , 'r' ) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# 7. Find and replace a word in a file
with open("test.txt" , 'r' ) as file:
    content = file.read()
    content = content.replace("Hello" , "Hi")
    print(content)

# 8. Check if a file exists before opening it
import os

if os.path.exists("test.txt"):
    with open("test.txt" , 'r' ) as file:
        content = file.read()
        print(content)

# 9. Read JSON data from a file and print specific fields
import json

with open("test.json" , 'r' ) as file:
    data = json.load(file)
    print(data["name"])
    print(data["age"])


# 10. Merge the contents of two text files into a new file
with open("test.txt" , 'r' ) as file:
    content1 = file.read()
    with open("test2.txt" , 'r' ) as file2:
        content2 = file2.read()
        with open("test3.txt" , 'w' ) as file3:
            file3.write(content1 + content2)
            