"""This script will find all word-pair palingrams in a dictionary file

Pseudocode:
    Load dictionary as a list of words
    Start an empty list to hold palingrams
    For word in word list:
        Get length of word
        If length > 1:
            Loop through the letters in the word:
                IF reversed word fragment at front of word is in word list and
                letters after form a palindromic sequence:
                    Append word and reversed word to palingram list
                IF reversed word fragment at end of word is in word list and
                letters before form a palindromic sequence:
                    Append reversed word and word to palingram list
    Sort palingram list alphabetically
    Print word-pair palingrams from palingram list

"""

import load_dictionary as ld

word_list = ld.load('words.txt')

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    for word in word_list:
        end = len(word)
        reverse_word = word[::-1]
        if end > 1:
            for i in range(end):
                if (word[i:] == reverse_word[:end-i] and reverse_word[end-i:]
                        in word_list):
                    pali_list.append((word, reverse_word[end-i:]))
                if (word[:i] == reverse_word[end-i:] and reverse_word[:end-i]
                        in word_list):
                    pali_list.append((reverse_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
