import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text data
documents = [
    "Machine learning is amazing",
    "Deep learning is a subset of machine learning",
    "Natural language processing and deep learning go hand in hand"
]

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer()

# Transform the text data into a TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(documents)

# Convert to DataFrame for better visualization
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())

print("\nTF-IDF Representation:")
print(tfidf_df)
