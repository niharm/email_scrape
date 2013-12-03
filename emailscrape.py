import cmd, getpass, webbrowser
import re
import urllib
from bs4 import BeautifulSoup
from pygmail import *
import string
import sys
from collections import Counter

 
def do_login():
    
    emails = ['']

    print "Authenticating account..."
    
    g = pygmail()
    email = 'XXXXXX@XXXXXX.XXX'
    password = "XXXXXXXXXXXXX"
    g.login(email,password)
    
    print "Done"
    return g


def write_info(g, wire):

    print "Email: " + g.user_email.upper()
    print "Downloading: " + wire

    wire_file = open('data/' + wire + '.tsv', 'w')
    wire_file.write('#\tName\tEmail\tDate\tWeekday\tTime\tSubject\tSuspect Score \n')

    wire_words = open('data/words_' + wire + '.txt', 'w')


    messages = g.fetchUnreadMessages(wire)

    count = 1

    people = Counter()

    listserv_address = wire + '@princeton.edu'
    print listserv_address

    for msg in messages:

       if msg['To'].lower() == listserv_address:
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


            #get spam score (specifically 'suspect score')
            spamdetails = msg['X-Proofpoint-Spam-Details']
            if spamdetails:
                # get spam score
                start = string.find(spamdetails, "suspectscore=")
                end = string.find(spamdetails, " phishscore=")
                suspectscore = spamdetails[(start + 13):end]

            else: 
                suspectscore = -1

            wire_words.write(str(msg))

            wire_file.write(str(count) + '\t')
            wire_file.write(name + '\t')
            wire_file.write(subject + '\t')
            wire_file.write(address + '\t')
            wire_file.write(str(date) + '\t')
            wire_file.write(day_of_week + '\t')
            wire_file.write(time + '\t')
            wire_file.write(str(suspectscore) + '\n')


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
    
    listservs = ['re-innformer', 'whitmanwire', 'wilsonwire', 'rockywire', 'matheymail', 'butlerbuzz']

    for listserv in listservs:
        g = do_login()
        write_info(g, listserv)

    print("Done!")