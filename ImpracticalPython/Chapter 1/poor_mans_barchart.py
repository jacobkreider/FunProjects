"""This module will count each unique character in a string and return a
pretty printed dict list that resembles a bar chart.
"""
from collections import defaultdict
from pprint import pprint

chart_data = defaultdict(list)

def main():
    """Inputs text from user and returns the 'bar chart'."""
    text = input("Type the sentence you would like analyzed:\n\n")
    text = text.lower()


    for letter in text:
        chart_data[letter] += letter

    if ' ' in chart_data:
        del chart_data[' ']

    return chart_data

if __name__ == "__main__":
    main()

pprint(chart_data)