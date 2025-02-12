# Student disct
student_dict = {"Alice": 25, "Bob": 22, "Charlie": 23}


# Sort dictionary by values
def sort_dict_by_values(dict):
    return dict( sorted(dict.items(), key=lambda item: item[1]))

print(sort_dict_by_values(student_dict))