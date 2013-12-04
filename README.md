README for Email Scrape
============
Nihar Madhavan
12/02/2013

============
Introduction
============

These are the Python scripts used in the "Listserv Scrape" project at http://www.princeton.edu/~madhavan/Listservs/.

They can be used to analyze any set of emails you have! (group 
the emails you want to analyze in a folder). 

Emailscape.py can be modified to download any configuration of data from emails!


=====
Usage
=====

Before Running
-------------------------
--- Group all email to be analyzed into folders (which can be accessed by IMAP)
--- Update variables in programs
--- Create a folder 'data in '

Scrape Emails
-------------------------
--- Run "emailscrape.py" after updating variables
------ Scrapes messages, likes, datetime submission, and tagged users from a given Facebook url, with a given Facebook access code.
------ Creates a file "data/[listserv].csv" and outputs sender name and email, date, weekday, time, and subject for each email 
------ Creates a file "data/people_in_[listserv].csv" and outputs unique senders and how many emails each sent. 


Count Subjects or Words
-------------------------
If you are counting senders across multiple listservs, you may need to count senders together to ensure there are not duplicates.

- Run "sum_of_people.py" after updating filenames
--- Will read in "data/people in_listserv.csv" files and count emails across all lists
--- Will output totals to "data/allpeople.csv"

Count Subjects or Words
-------------------------
- Run "top_word_counter.py" after updating filenames
--- Will count words and output most common words (ex. most common words in subjects)

Credit
-------------------------
--- Credit to Shubhro Saha (github.com/shbhrsaha/) for pygmail.py scripts. 
