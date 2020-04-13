"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

#Creating a dictionary
hours = dict()
#Initialize the count
count =0
#Create an empty list
allhours=[]


#import io
#fname = input("Enter file:")
#if len(fname) < 1 : fname = "mbox-short.txt"
handle = open('mbox-short.txt')
#handle = ['From rajiv@gmail ejSAK 23kASJ  8q32 W', "asda sasda", 'From rohan@yahoomail eqwe qwe3 34','From rohan@yahoomail','From rohan@yahoomail','From rajiv@gmail']
#handle = io.StringIO()

for lin in handle:
    lin = lin.rstrip()
    #print(lin)
    if lin.startswith('From '):
        words = lin.split()
        #print('words:-',words)
        email = words[5]
        hourmark = email.split(':')
        allhours.append(hourmark[0])
#print(allhours)    # this is a list
#print('ALL email:-',allmails)
#creating dict
for ids in allhours:  #traverse through list 
    if ids not in hours: #if list element not in dict called hours
        hours[ids]=1. #mark 1
    else:
        hours[ids] = hours[ids] + 1 #increment the counter
#print('dict hours', hours)

newlst = sorted(hours.items())

for key,val in newlst:
  print(key,int(val))

        
#print(frequent_word, frequency) 