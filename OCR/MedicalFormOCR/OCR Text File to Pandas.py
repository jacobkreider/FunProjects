# Import libraries
import re
import os

os.chdir('/home/jacob/DataScience/FunProjects/OCR/MedicalFormOCR')

import re
import pandas as pd

# Open the file for reading
#with open('out_text.txt') as fd:

    # Iterate over the lines
 #   for line in fd:

        # Capture one-or-more characters of non-whitespace after the initial match
  #      match = re.search(r'Hema : (\S+)', line)

        # Did we find a match?
   #     if match:
            # Yes, process it
    #        weather = match.group(1)
     #       print('weather: {}'.format(weather))

print("Hello")

#with open("out_text.txt") as openfile:
 #   for line in openfile:
  #      for part in line.split():
   #         if "NEUT" in part:
    #            NEUT = pd.DataFrame(line)

initializeColums = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data = pd.read_csv('out_text.txt', names = initializeColums, sep =" ", header=None)
print(data)