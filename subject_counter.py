import re
from collections import Counter

top_word_count = 300

wire_subjects = open('data/subjects_on_sunday.tsv', 'r')

text = wire_subjects.read()

# get the most common words in a list
words = re.findall('\w\w\w+', text.lower())
word_counter = Counter(words).most_common(top_word_count)

#save the top words in a file
f_words = open('data/top_subjectwords_onsunday' + '.csv', 'w')
for i in range(0, top_word_count):
    word = word_counter[i][0]
    count = word_counter[i][1]
    f_words.write(word + ', ' + str(count) + '\n')
f_words.close()