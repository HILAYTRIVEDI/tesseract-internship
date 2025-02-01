tuples_list = [(1, 2), (3, 1), (5, 7), (9, 4)]

# Sorting by second element
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(f"Sorted list by second element: {sorted_list}")
