import re
from collections import Counter

listservs = ['re-innformer', 'whitmanwire', 'wilsonwire', 'rockywire', 'matheymail', 'butlerbuzz']

top_word_count = 2000

text = ""

#for listserv in listservs:

#wire_words = open('data/words_' + listserv + '.txt', 'r')
wire_words = open('data/email_subjects.tsv', 'r')


text += wire_words.read()

# get the most common words in a list
words = re.findall('\w\w\w+', text.lower())
word_counter = Counter(words).most_common(top_word_count)

#save the top words in a file
f_words = open('data/topwords' + '.csv', 'w')
for i in range(0, top_word_count):
    word = word_counter[i][0]
    count = word_counter[i][1]
    f_words.write(word + ', ' + str(count) + '\n')
f_words.close()