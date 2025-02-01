# 1. Write a program that reverses a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello, World!"))

# 2. Implement a script that removes vowels from a string.
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])

print(remove_vowels("This is a test sentence."))

# 3. Write a function to check if two strings are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))

# 4. Create a program that counts the number of words in a string.
def count_words(s):
    return len(s.split())

print(count_words("The quick brown fox jumps over the lazy dog."))

# 5. Implement a script that capitalizes the first letter of each word in a string.
def capitalize_words(s):
    return s.title()

print(capitalize_words("hello world! this is python."))

# 6. Write a script to find the most frequent character in a string.
from collections import Counter

def most_frequent_char(s):
    count = Counter(s.replace(" ", ""))
    return count.most_common(1)[0]

print(most_frequent_char("hello world"))

# 7. Create a regex pattern to validate an email address.
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))

# 8. Write a program to extract all numbers from a given string.
def extract_numbers(s):
    return re.findall(r'\d+', s)

print(extract_numbers("There are 12 apples and 24 oranges."))

# 9. Implement a function that replaces all spaces in a string with hyphens.
def replace_spaces(s):
    return s.replace(" ", "-")

print(replace_spaces("replace all spaces with hyphens"))

# 10. Create a script that checks if a given string is a valid palindrome.
def is_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))
