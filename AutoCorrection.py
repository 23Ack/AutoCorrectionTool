!pip install nltk
import nltk 
from nltk.metrics import edit_distance
from nltk.corpus import words

nltk.download('words')

def correct_word(word):
    # Get a list of English words from the NLTK corpus
    english_words = set(words.words())

    # Check if the word is already in the English words list
    if word.lower() in english_words:
        return word  # The word is correct

    # Find the closest word based on Levenshtein Distance
    min_distance = float('inf')
    closest_word = None
    for english_word in english_words:
        distance = edit_distance(word.lower(), english_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = english_word

    return closest_word

# Test the spell checker
misspelled_word = input("Give the word!!: ")
corrected_word = correct_word(misspelled_word)
print(f"Given word: {misspelled_word}")
print(f"Corrected word: {corrected_word}")
