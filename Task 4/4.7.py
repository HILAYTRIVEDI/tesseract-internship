def check_character(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

char = input("Enter a character: ")
print(f"The character is a {check_character(char)}.")
