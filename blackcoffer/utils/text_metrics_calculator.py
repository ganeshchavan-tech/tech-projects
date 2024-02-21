from utils.common import read_file, zeros_dict
from nltk.corpus import stopwords
import string
import re
from .constant import PRONOUN_REGEX_STR

def count_syllable(words):
    syllable_count_dict = {}
    for word in words:
        syllable_count = 0
        if word[-2:] != 'es' or word[-2:] != 'ed':
            for char in word:
                if char.lower() in 'euioa':
                    syllable_count += 1
            syllable_count_dict[word] = syllable_count
    return syllable_count_dict

    
def cleaned_words_count(words_list):
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    words_without_punctuation = [word for word in words_list if word not in string.punctuation and word.lower() not in stop_words]
    return len(words_without_punctuation)


def count_personal_pronouns(word_list):
    # Join the words into a single string
    text = ' '.join(word_list)

    # Define a regex pattern for personal pronouns
    pronoun_pattern = re.compile(PRONOUN_REGEX_STR, flags=re.IGNORECASE)

    # Find all matches using the regex pattern
    matches = pronoun_pattern.findall(text)

    # Count the occurrences
    pronoun_counts = {}
    for pronoun in matches:
        pronoun_counts[pronoun.lower()] = pronoun_counts.get(pronoun.lower(), 0) + 1

    return sum(pronoun_counts.values())


def calculate_positive_negative_score(filtered_words):
    positive_words = read_file('./MasterDictionary/positive-words.txt').split()
    negative_words = read_file('./MasterDictionary/negative-words.txt').split()
    positive_words_dict = zeros_dict(positive_words)
    negative_words_dict = zeros_dict(negative_words)

    for word in filtered_words:
        if word in positive_words:
            positive_words_dict[word] += 1

        if word in negative_words:
            negative_words_dict[word] -= 1
    
    positive_score = sum(positive_words_dict.values())
    negative_score = sum(negative_words_dict.values()) * -1

    return {"positive_score" : positive_score,"negative_score" : negative_score}


def calculate_polarity_score(positive_score, negative_score):
    polarity_score = (positive_score - negative_score)/((positive_score + negative_score) + 0.000001)
    return polarity_score


def calculate_subjectivity_score(filtered_words,positive_score,negative_score):
    subjectivity_score = (positive_score + negative_score)/((len(filtered_words)) + 0.000001)
    return subjectivity_score


def calculate_average_sentence_length(word_tokens,sentence_tokens):
    average_sentence_length = len(word_tokens)/len(sentence_tokens)
    return average_sentence_length


def calculate_complex_word_count(syllables_count_dict):
    complex_words_dict = dict(filter(lambda item: item[1] > 2, syllables_count_dict.items()))
    complex_words_count = sum(complex_words_dict.values())
    return complex_words_count


def calculate_fog_index(average_sentence_length,percentage_complex_words):
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    return fog_index


def calculate_average_word_length(word_tokens):
    average_word_length = len(''.join(word_tokens))/len(word_tokens)
    return average_word_length
