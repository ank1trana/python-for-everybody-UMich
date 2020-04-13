"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

handle = open('mbox-short.txt')
mailers = dict()
count =0
allmails=[]
#import io
#fname = input("Enter file:")
#if len(fname) < 1 : fname = "mbox-short.txt"
#handle = open('/Users/ankit/Downloads/mbox-short.txt')
#handle = ['From rajiv@gmail ejSAK 23kASJ  8q32 W', "asda sasda", 'From rohan@yahoomail eqwe qwe3 34','From rohan@yahoomail','From rohan@yahoomail','From rajiv@gmail']
#handle = io.StringIO()

for lin in handle:
    lin = lin.rstrip()
    #print(lin)
    if lin.startswith('From '):
        words = lin.split()
        #print('words:-',words)
        email = words[1]
        allmails.append(email)
        
#print('ALL email:-',allmails)
#creating dict
for ids in allmails:
    if ids not in mailers:
        mailers[ids]=1
    else:
        mailers[ids] = mailers[ids] + 1
#print('d mailers', mailers)        

frequent_word = None
frequency = None

for mailids,counter in mailers.items():
    if frequency is None or counter > frequency:
        frequency = counter
        frequent_word = mailids
        
print(frequent_word, frequency) 