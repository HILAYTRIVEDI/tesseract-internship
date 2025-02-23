# Tokenize and clean textual data with spaCy

import spacy

nlp = spacy.load('en_core_web_sm')

text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."

doc = nlp(text)

# Step 2: Remove stopwords and punctuation, and perform lemmatization
tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

print(tokens)
print('Original Text', text)
