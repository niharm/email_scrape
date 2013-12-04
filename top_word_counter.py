################################################
# top_word_counter.py
# Nihar Madhavan
# December 2013
#
# Lists the most common words in specified file
# and how many times they were used.
#
################################################

# UPDATE THESE VARIABLES
filepath = 'filepath' #specify body of text to be read in
output_filepath = 'output_filepath' #file to save results
top_word_count = 300 #number of top words to be printed

################################################

import re
from collections import Counter

in_file = open(filepath, 'r')

text = in_file.read()

# get the most common words in a list
words = re.findall('\w+', text.lower())
word_counter = Counter(words).most_common(top_word_count)

#save the top words in a file
f_words = open(output_filepath, 'w')
for i in range(0, top_word_count):
    word = word_counter[i][0]
    count = word_counter[i][1]
    f_words.write(word + ', ' + str(count) + '\n')
f_words.close()

