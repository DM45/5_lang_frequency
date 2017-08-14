import os
import re
from collections import Counter


def load_data(filepath, top_count):
    if not os.path.exists(filepath) or not top_count.isdigit():
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, top_count):
    words = re.findall(r'\w+', text.lower())
    most_freq_words = [
        word[0] for word in
        Counter(words).most_common(int(top_count))]
    return most_freq_words


def get_output_data(checks_marker):
    if checks_marker is None:
    	print('Wrong filepath/filename or count is not digits')
    else:
        print ('List of frequent words: ')
        print(' '.join(get_most_frequent_words(_load_data, _top_count)))


if __name__ == '__main__':
    _filepath = input('Enter filepath to file: ')
    _top_count = input('Enter count of most frequent words: ')
    _load_data = load_data(_filepath, _top_count)
    _checks_marker = get_output_data(_load_data)
