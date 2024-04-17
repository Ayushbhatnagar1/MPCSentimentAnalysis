import os
import PyPDF2
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import csv

import os
import PyPDF2
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import csv
import string
import syllapy

def calculate_readability_score(text):
    num_monosyllabic_words = count_monosyllabic_words(text)
    num_words = count_words(text)
    num_sentences = count_sentences(text)
    FJP = 1.599 * (num_monosyllabic_words / 100) - 1.015 * (num_words / num_sentences) - 31.517
    return FJP

# Function to count monosyllabic words
def count_monosyllabic_words(text):
    words = text.split()
    monosyllabic_count = sum(1 for word in words if syllapy.count(word) == 1)
    return monosyllabic_count

# Function to count words
def count_words(text):
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    return len(words)

# Function to count sentences
def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

# Define the path to the folder containing the PDF files
folder_path = r'C:\Users\Ayush Bhatnagar\Desktop\Plaksha\sem4\MLPR\moms'

# Load sentiment dictionaries (Implement these functions based on your dictionaries)
# ...

# Initialize data storage
data = []

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(folder_path, file_name)
        date = re.search(r'(\d{2}\d{2}\d{2})\.pdf', file_name)
        if date:
            date_str = date.group(1)
        
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''.join(page.extract_text() for page in reader.pages)
        text_without_hindi = remove_hindi(text)
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(text_without_hindi.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        cleaned_text = ' '.join(filtered_words)
        
        # Calculate sentiment scores (implement this function based on your sentiment analysis)
        # ...
        
        # Calculate the readability score
        readability_score = calculate_readability_score(cleaned_text)
        
        # Append the cleaned text, sentiment scores, and readability score to the data storage
        data.append((date_str, cleaned_text, sentiment_score, positive_score, negative_score, neutral_proportion, readability_score))

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=['Date', 'Cleaned_Text', 'Sentiment_Score', 'Positive_Score', 'Negative_Score', 'Neutral_Proportion', 'Readability_Score'])

# Save the DataFrame to an Excel file
output_path = r'C:\Users\Ayush Bhatnagar\Desktop\Plaksha\sem4\MLPR\moms\rbi_mpc_minutes.xlsx'
df.to_excel(output_path, index=False, engine='xlsxwriter')

# Define the path to the folder containing the PDF files
folder_path = r'C:\Users\Ayush Bhatnagar\Desktop\Plaksha\sem4\MLPR\moms'

# Initialize data storage
data = []

# Function to remove Hindi characters from the text
def remove_hindi(text):
    return ' '.join(word for word in text.split() if not re.search('[\u0900-\u097F]', word))

# Load sentiment dictionaries
def load_lm_dictionary(lm_path):
    lm_dict = {}
    with open(lm_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lm_dict[row['Word'].lower()] = {'positive': int(row.get('Positive', 0)),
                                             'negative': int(row.get('Negative', 0))}
    return lm_dict

def load_correa_dictionary(correa_path):
    correa_df = pd.read_excel(correa_path)
    correa_dict = {}
    for index, row in correa_df.iterrows():
        word = str(row['Word']).lower().strip()
        positive_score = row['Positive'] if not pd.isna(row['Positive']) else 0
        negative_score = row['Negative'] if not pd.isna(row['Negative']) else 0
        correa_dict[word] = {'positive': int(positive_score),
                             'negative': int(negative_score)}
    return correa_dict

def load_neutral_dictionary(neutral_path):
    neutral_df = pd.read_excel(neutral_path)
    neutral_dict = {row['Word'].lower(): 'neutral' for index, row in neutral_df.iterrows()}
    return neutral_dict

def combine_dictionaries(*dicts):
    combined_dict = {}
    for d in dicts:
        for word, scores in d.items():
            if word not in combined_dict:
                combined_dict[word] = scores
            else:
                combined_dict[word]['positive'] += scores.get('positive', 0)
                combined_dict[word]['negative'] += scores.get('negative', 0)
    return combined_dict

lm_dictionary = load_lm_dictionary('lm.csv')
correa_dictionary = load_correa_dictionary('correa1.xlsx')
neutral_dictionary = load_neutral_dictionary('neutral.xlsx')

combined_dictionary = combine_dictionaries(lm_dictionary, correa_dictionary)

# Sentiment scoring function
def score_document(document):
    words = nltk.word_tokenize(document.lower())
    positive_words = []
    negative_words = []
    neutral_words = []

    for word in words:
        if word in combined_dictionary:
            if combined_dictionary[word].get('positive', 0) > 0:
                positive_words.append(word)
            if combined_dictionary[word].get('negative', 0) > 0:
                negative_words.append(word)
        if word in neutral_dictionary:
            neutral_words.append(word)

    positive_score = len(positive_words)
    negative_score = len(negative_words)
    neutral_count = len(neutral_words)

    total_words = len(words)
    sentiment_score = (positive_score - negative_score) / total_words if total_words > 0 else 0
    neutral_proportion = neutral_count / total_words if total_words > 0 else 0

    return sentiment_score, positive_score, negative_score, neutral_proportion

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(folder_path, file_name)
        date = re.search(r'(\d{2}\d{2}\d{2})\.pdf', file_name)
        if date:
            date_str = date.group(1)

        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''.join(page.extract_text() for page in reader.pages)
        text = remove_hindi(text)
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(text.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        cleaned_text = ' '.join(filtered_words)
        sentiment_score, positive_score, negative_score, neutral_proportion = score_document(cleaned_text)
        data.append((date_str, cleaned_text, sentiment_score, positive_score, negative_score, neutral_proportion))

df = pd.DataFrame(data, columns=['Date', 'Cleaned_Text', 'Sentiment_Score', 'Positive_Score', 'Negative_Score', 'Neutral_Proportion'])
print(df.head(10))

output_path = r'C:\Users\Ayush Bhatnagar\Desktop\Plaksha\sem4\MLPR\moms\rbi_mpc_minutes.xlsx'
df.to_excel(output_path, index=False, engine='xlsxwriter')
