import io
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import pandas as pd
import re
file_path = 'file1.txt'  

with io.open(file_path, 'r', encoding='utf8') as file:
    text_data = file.read()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

preprocessed_text = preprocess_text(text_data)

# Step 3: Calculate TF-IDF features
tfidf_vectorizer = TfidfVectorizer(max_features=500,
                                   stop_words=stopwords.words('english'),
                                   ngram_range=(1, 2))

tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_text])

# The 'tfidf_matrix' now contains the TF-IDF features which can be used for further analysis or modeling

# To view the feature names (words or n-grams)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Convert the matrix to a DataFrame for better readability (optional)
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

print(tfidf_df)
