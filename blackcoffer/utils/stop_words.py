import os
from .common import read_file
from .constant import STOPWORD_FOLDER_PATH

stopword_files = os.listdir(STOPWORD_FOLDER_PATH)

def get_custom_stopwords():
    custom_stopwords = set()
    for file_name in stopword_files:
        stopwords_str = read_file(f'{STOPWORD_FOLDER_PATH}/{file_name}')
        custom_stopwords |= set(stopwords_str.split())
    return list(custom_stopwords)
