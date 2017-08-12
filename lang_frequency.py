import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    most_freq_words = [word[0] for word in Counter(words).most_common(10)]
    return ' '.join(most_freq_words)


if __name__ == '__main__':
    _filepath = input('Enter filepath to file: ')
    _load_data = load_data(_filepath)
    print('List of 10 frequent words: ')
    print(get_most_frequent_words(_load_data))
