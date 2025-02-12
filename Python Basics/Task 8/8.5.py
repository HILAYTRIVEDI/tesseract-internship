# Create a dictionary with student names and grades, and print students with grade 'A'
students = {'John': 'A', 'Alice': 'B', 'Bob': 'C', 'Dylan': 'A', 'Eva': 'B'}


def print_students_with_grade_a(students):
    for student, grade in students.items():
        if grade == 'A':
            print(student)

print_students_with_grade_a(students)