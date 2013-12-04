################################################
# sum_of_people.py
# Nihar Madhavan
# December 2013
#
# Specific task for listserv scraping project.
# Adds together the people and emails sent
# accross listservs. 
#
################################################

# UPDATE THESE VARIABLES
listservs = ['re-innformer', 'whitmanwire', 'wilsonwire', 'rockywire', 'matheymail', 'butlerbuzz']

################################################

import csv
from collections import Counter

allpeople = Counter()

# go through every listserv and add people to count
for listserv in listservs:

	#open people and counts 
	wire_people = open('data/people_in_' + listserv + '.csv', 'r')

	# save them in counter
	reader = csv.reader(wire_people)
	for row in reader:
		allpeople[row[0]] += int(row[1])

	# close file
	wire_people.close()

#save the people with total counts in a csv file
wire_people = open('data/allpeople.csv', 'w')
for person in allpeople:
    wire_people.write(str(person) + ', ' + str(allpeople[person]) + '\n')
    
wire_people.close()