# My list 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ger the second largest number from the list
def get_second_largest_number(my_list):

    # Check for duplicates and remove it
    my_list = list(set(my_list))
    my_list.sort()
    return my_list[-2] if len(my_list) > 1 else None


second_largest = get_second_largest_number(my_list)

print(f"The second largest number in the list is: {second_largest}")