import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def validation_data(loaded_data, digit_check):
    validate_error = 0
    if loaded_data is None:
        print('Wrong filepath or wrong filename')
        validate_error = 1
    if not digit_check.isdigit():
        validate_error = 1
        print('Wrong count')
    if not validate_error:
        return 1


def get_most_frequent_words(text, top_count):
    words = re.findall(r'\w+', text.lower())
    most_freq_words = [
        word[0] for word in
        Counter(words).most_common(int(top_count))]
    return most_freq_words


def prepare_output(output_frequent_words):
	return ' '.join(output_frequent_words)


if __name__ == '__main__':
    _filepath = input('Enter filepath to file: ')
    _top_count = input('Enter count of most frequent words: ')
    _load_data = load_data(_filepath)
    _validation_data = validation_data(_load_data, _top_count)
    if _validation_data:
        print(prepare_output(get_most_frequent_words(_load_data, _top_count)))
