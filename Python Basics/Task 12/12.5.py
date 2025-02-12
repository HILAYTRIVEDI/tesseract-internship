# Write a script that handles multiple exceptions (e.g., IndexError, KeyError).

def handle_exceptions():
    my_list = [10, 20, 30]
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    try:
        # Trying to access an index that doesn't exist in the list
        print("Accessing list element at index 5:")
        print(my_list[5])  # This will raise an IndexError

        # Trying to access a key that doesn't exist in the dictionary
        print("Accessing dictionary key 'z':")
        print(my_dict['z'])  # This will raise a KeyError

    except IndexError as e:
        print(f"IndexError: {e}")

    except KeyError as e:
        print(f"KeyError: {e}")

    except Exception as e:
        # This will catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

    else:
        # This runs only if no exceptions are raised
        print("No errors occurred!")

    finally:
        # This runs no matter what (even if an error happens)
        print("Finished trying to access elements.")

# Run the function
handle_exceptions()
