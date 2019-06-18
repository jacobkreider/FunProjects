"""This script will load a text file and find palindromes within

Pseudocode:
    -Load dictionary file as a list of words
    -Create an empty list to hold palindromes
    -Loop through each word in word list:
        -If word sliced forward == word sliced backward:
            -Append word to palindrome list
    Print palindrome list

"""
import os
# Change working directory to location of load_dictionary abd words list
os.chdir('/home/jacob/DataScience/FunProjects/ImpracticalPython/Chapter 2')

import load_dictionary as ld

word_list = ld.load('words.txt')
palindromes_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindromes_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(palindromes_list)))
print(*palindromes_list, sep='\n')
