def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    return cleaned_text == cleaned_text[::-1]

def count_words(text):
    return len(text.split())

def remove_whitespace(text):
    return text.replace(" ", "")

def capitalize_words(text):
    return text.title()
