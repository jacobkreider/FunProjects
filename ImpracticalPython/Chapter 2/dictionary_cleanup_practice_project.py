"""Removes one-letter words from a loaded dictionary file"""

import load_dictionary as ld

word_file = sorted(ld.load('words.txt'))


def one_letter_word_count(word_list):
    """Return a count of all single letter words."""
    count = 0
    for word in word_list:
        if len(word) == 1:
            count += 1
    return count

print("\nThere are {} words of length 1 in the word file\n\n".format(
    one_letter_word_count(word_file)))

def remove_one_letter_words(word_list):
    """Return the word list with all single letter words removed"""
    new_words = []
    for word in word_list:
        if len(word) > 1:
            new_words.append(word)
    return new_words

new_word_file = remove_one_letter_words(word_file)

print("\nThere are now {} words of length 1 in the word file.".format(
    one_letter_word_count(new_word_file)))
