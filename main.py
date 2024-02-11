import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the trained model
model = load_model('next_word_model.h5')  # Update the path to your model

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Ensure you have the correct max_sequence_len used during training
max_sequence_len = 20  # Update this with the actual value used during training

def predict_next_words(text, n=3):
    sequence = tokenizer.texts_to_sequences([text])[0]
    sequence = pad_sequences([sequence], maxlen=max_sequence_len - 1, padding='pre')
    predictions = model.predict(sequence, verbose=0)[0]

    top_indices = np.argsort(predictions)[-n:][::-1]
    top_words = []
    for i in top_indices:
        for word, index in tokenizer.word_index.items():
            if index == i:
                top_words.append(word)
                break

    return top_words


# Example usage
print(predict_next_words("The weather today is", 5))
print(predict_next_words("Despite the heavy rains, the event continued", 5))
print(predict_next_words("On top of the", 5))