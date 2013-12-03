import csv
from collections import Counter

listservs = ['re-innformer', 'whitmanwire', 'wilsonwire', 'rockywire', 'matheymail', 'butlerbuzz']

allpeople = Counter()


for listserv in listservs:


	#save the people with tags and the number in a csv file
	wire_people = open('data/people_in_' + listserv + '.csv', 'r')

	reader = csv.reader(wire_people)

	for row in reader:
		allpeople[row[0]] += int(row[1])


	wire_people.close()

#save the people with tags and the number in a csv file
wire_people = open('data/allpeople' + '.csv', 'w')
for person in allpeople:
    wire_people.write(str(person) + ', ' + str(allpeople[person]) + '\n')
    
wire_people.close()