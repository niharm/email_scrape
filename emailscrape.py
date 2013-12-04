################################################
# emailscape.py
# Nihar Madhavan
# December 2013
#
# This will download all the messages in the folders
# for the account specified below. See readme for 
# usage and file creation.
#
# Note: this will check every message in the folder.
# Sometimes, this can cause problems if you have tagged
# one message in a conversation but every message
# in that converation will now be analyzed.
################################################

# UPDATE THESE VARIABLES

#account info
email = "email@domain.com"
password = "password"

l#list of folders to be searched
folders = ['re-innformer', 'whitmanwire', 'wilsonwire', 'rockywire', 'matheymail', 'butlerbuzz']

################################################

import cmd, getpass, webbrowser
import re
import urllib
from bs4 import BeautifulSoup
from pygmail import *
import string
import sys
from collections import Counter

# logs into email
def do_login():
    
    emails = ['']

    print "Authenticating account..."
    
    g = pygmail()
    g.login(email,password)
    
    print "Authenticated!"
    return g

# writes info to files
def write_info(g, wire):

    print "Email: " + g.user_email.upper()
    print "Downloading: " + wire

    #files
    wire_file = open('data/' + wire + '.tsv', 'w')
    wire_file.write('#\tName\tEmail\tDate\tWeekday\tTime\tSubject\n')
    wire_words = open('data/words_' + wire + '.txt', 'w')

    # get messages
    messages = g.fetchMessages(wire)

    # counter variables
    count = 1
    people = Counter()

    for msg in messages:

            msgFromArray = email.utils.parseaddr(msg['From'])
            name = msgFromArray[0]
            address = msgFromArray[1]

            people[address]+=1

            date_str = msg['Date']
            date_tuple = email.utils.parsedate_tz(date_str)
            if date_tuple:
                d = datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                date = d.strftime("%m/%d/%y")
                day_of_week = d.strftime("%A")
                time = d.strftime("%H:%M")
            else:
                date = -1
                day_of_week = 'none'
                time = 'none'

            if msg['Subject']:
                subject = msg['Subject']
            else:
                subject = ""

            wire_words.write(str(msg))

            wire_file.write(str(count) + '\t')
            wire_file.write(name + '\t')
            wire_file.write(subject + '\t')
            wire_file.write(address + '\t')
            wire_file.write(str(date) + '\t')
            wire_file.write(day_of_week + '\t')
            wire_file.write(time + '\n')

            count += 1


    #save the people with tags and the number in a csv file
    wire_people = open('data/people_in_' + wire + '.csv', 'w')
    for person in people:
        wire_people.write(str(person) + ', ' + str(people[person]) + '\n')


    wire_file.close()
    wire_words.close()
    wire_people.close()

    print(str(count) + " Emails Downloaded!")


if __name__ == '__main__':

    for folder in folders:
        g = do_login()
        write_info(g, folder)

    print("All done!")