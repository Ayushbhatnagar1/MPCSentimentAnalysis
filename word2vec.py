# Ensure you have gensim installed: 
# !pip install gensim

import gensim
import io

# Load your RBI MPC minute text file
file_path = 'file1.txt'  # Change this to the path of your text file

with io.open(file_path, 'r', encoding='utf8') as file:
    mpc_text = file.readlines()

# Tokenization and simple preprocessing
mpc_text_processed = [gensim.utils.simple_preprocess(line) for line in mpc_text]

# Initialize the Word2Vec model
model = gensim.models.Word2Vec(
    window=10,    # Context window size
    min_count=2,  # Ignores words with total frequency lower than this
    workers=4,    # Number of CPU cores
)

# Build vocabulary from the processed text data
model.build_vocab(mpc_text_processed, progress_per=1000)

# Train the Word2Vec model
model.train(mpc_text_processed, total_examples=model.corpus_count, epochs=model.epochs)

# Finding words similar to a given word
similar_to_monetary = model.wv.most_similar("monetary", topn=10)
print(f"Words similar to 'monetary': {similar_to_monetary}")

# Checking similarity between words
similarity_rate = model.wv.similarity(w1="inflation", w2="economy")
print(f"Similarity between 'inflation' and 'economy': {similarity_rate}")

# Save the model for later use
model.save("rbi_mpc_minutes_word2vec.model")
