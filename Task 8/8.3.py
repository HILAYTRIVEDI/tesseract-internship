# Demo Directory 1
directory_one = {
    'file1': 100,
    'file2': 200,
    'file3': 300
}

# Demo Directory 2
directory_two = {
    'file4': 100,
    'file5': 200,
    'file6': 300
}


# Merge two dictionaries
def merge_two_dicts(dict1, dict2):
    print({**dict1})
    print({**dict2})
    return {**dict1, **dict2}


merged_directory =  merge_two_dicts(directory_one, directory_two)
print(merged_directory)