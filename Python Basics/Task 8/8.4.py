# Input string
sentence = "hello world hello python world"

# Convert string to list of words
words = sentence.split()

# Create a dictionary to store word frequencies
word_count = {}

# Count frequency of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Print word frequencies
print(f"Word frequencies: {word_count}")
