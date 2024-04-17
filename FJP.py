import syllapy
import string

def count_monosyllabic_words(text):
    # Tokenize the text into words
    words = text.split()
    
    # Count the number of monosyllabic words
    monosyllabic_count = sum(1 for word in words if syllapy.count(word) == 1)
    
    return monosyllabic_count

def count_words(sentence):
    # Remove punctuation and split the sentence into words
    words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
    
    return len(words)

def count_sentences(sentence):
    # Split the sentence into sentences based on common punctuation marks
    sentences = sentence.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings
    
    return len(sentences)

file_path = "d:\Ed\Plaksha/4th Semester\Machine Learning and Pattern Recognition\Project/file1.txt"
try:
    with open(file_path, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

num_monosyllabic_words = count_monosyllabic_words(text)
num_words = count_words(text)
num_sent = count_sentences(text) 

FJP = 1.599*(num_monosyllabic_words/100) - 1.015*(num_words/num_sent) - 31.517
print (f'Readability score: {FJP}')