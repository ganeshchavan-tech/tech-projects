from .common import read_file
from nltk import word_tokenize, sent_tokenize
from .stop_words import get_custom_stopwords
from .text_metrics_calculator import *
from .constant import DATA_FILE_PATH


def data_analyser(df):
    """
        Analyzes data from a DataFrame containing URL information and performs sentiment analysis,
        readability analysis, and other metrics on the associated text data.

        Args:
        - df (pd.DataFrame): A DataFrame with columns URL_ID and URL.

        Returns:
        A list of dictionaries, where each dictionary represents the analysis results for a URL.
        """
    
    # Get the list of stopwords from the StopWords folder
    custom_stopwords = get_custom_stopwords()
    all_article_score = list()

    # Iterate over the each row/URL_ID.
    for index, row in df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        
        try:
            # Sentiment Analysis:
            # Tokenization of fetched data. 
            article_data_str = read_file(DATA_FILE_PATH.format(url_id))
            word_tokens = word_tokenize(article_data_str)
            sentence_tokens = sent_tokenize(article_data_str)
            filtered_words = [word for word in word_tokens if word not in custom_stopwords]

            # Calculation of positive and negative score from text.
            positive_negative_score = calculate_positive_negative_score(filtered_words)
            positive_score = positive_negative_score["positive_score"]
            negative_score = positive_negative_score["negative_score"]

            # Calculation of polarity and subjectivity score.
            polarity_score = calculate_polarity_score(positive_score, negative_score)
            subjectivity_score = calculate_subjectivity_score(filtered_words,positive_score,negative_score)

            # Analysis of Readability

            # Average Sentence Length / Average Number of Words Per Sentence
            average_sentence_length = calculate_average_sentence_length(word_tokens,sentence_tokens)

            # Syllable Count Per Word, Dictionary of words and syllable count
            syllables_count_dict = count_syllable(word_tokens)
            syllables_count = sum(syllables_count_dict.values())

            # Complex Word Count
            complex_words_count = calculate_complex_word_count(syllables_count_dict)

            # Percentage of Complex words
            percentage_complex_words = complex_words_count / len(word_tokens)

            # Fog Index
            fog_index = calculate_fog_index(average_sentence_length,percentage_complex_words)

            # Cleaned words by filtering NLTK Stopwords and Punctuation.
            cleaned_words_count_ = cleaned_words_count(word_tokens)

            personal_pronouns_count = count_personal_pronouns(word_tokens)

            # Average word length
            average_word_length = calculate_average_word_length(word_tokens)

            article_score = {
                            "URL_ID":url_id,
                            "URL":url,
                            "POSITIVE SCORE":positive_score,
                            "NEGATIVE SCORE":negative_score,
                            "POLARITY SCORE":polarity_score,
                            "SUBJECTIVITY SCORE":subjectivity_score,
                            "AVG SENTENCE LENGTH":average_sentence_length,
                            "PERCENTAGE OF COMPLEX WORDS":percentage_complex_words,
                            "FOG INDEX":fog_index,
                            "AVG NUMBER OF WORDS PER SENTENCE":average_sentence_length,
                            "COMPLEX WORD COUNT":complex_words_count,
                            "WORD COUNT":cleaned_words_count_,
                            "SYLLABLE PER WORD":syllables_count,
                            "PERSONAL PRONOUNS":personal_pronouns_count,
                            "AVG WORD LENGTH":average_word_length}
            
            all_article_score.append(article_score)

        except Exception as e:
            print(f"Error occured: {e}")

    return all_article_score