import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, top_count):
    words = re.findall(r'\w+', text.lower())
    most_freq_words = [
        word[0] for word in
        Counter(words).most_common(top_count)]
    return ' '.join(most_freq_words)


if __name__ == '__main__':
    _filepath = input('Enter filepath to file: ')
    _top_count = int(input('Enter count of top words: '))
    _load_data = load_data(_filepath)
    print('List of ' + str(_top_count) + ' frequent words: ')
    print(get_most_frequent_words(_load_data, _top_count))
