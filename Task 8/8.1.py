# Create a diractory
student_dict = {"Alice": 25, "Bob": 22, "Charlie": 23}

# Adding a new student
student_dict["David"] = 24

# Update the record of Bob
student_dict["Bob"] = 24

# Remove the record of Alice
student_dict.pop("Alice")

# Print the record of Charlie
print(f" Charlie is {student_dict['Charlie']} years old")