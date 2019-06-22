"""This script will load a text file and
find palindromes within using recursion

Pseudocode:
    -Load dictionary file as a list of words
    -Create an empty list to hold palindromes
    -Loop through each word in word list:
        -If word is of length 1, then is a palindrome (base case)
        -Elif the first and last letters are not the same, is not palindrome
        -Apply recursive algorithm to what's left of word after removing
        1st and last letters.
        -Continue until base case is satisfied
    Print palindrome list

"""

import load_dictionary as ld

word_list = ld.load('words.txt')
palindromes_list = []


def ispalindrome(word):
    """Uses recursion to find palindromes in list."""
    if len(word) < 2:
        return palindromes_list.append(whole_word)
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])

for w in word_list:
    whole_word = w
    ispalindrome(w)


print("\nNumber of palindromes found = {}\n".format(len(palindromes_list)))
print(*palindromes_list, sep='\n')
