import gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Sample text corpus
sentences = [
    "Machine learning is amazing",
    "Deep learning is a subset of machine learning",
    "Natural language processing and deep learning go hand in hand"
]

# Tokenize sentences into words
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train Word2Vec model
word2vec_model = Word2Vec(sentences=tokenized_sentences, vector_size=50, window=5, min_count=1, workers=4)

# Get vector for a word
vector = word2vec_model.wv['learning']  # Word embedding for "learning"

print("\nWord2Vec Representation for 'learning':")
print(vector)
