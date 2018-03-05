from urllib.request import urlretrieve
import urllib.parse
import os.path
import re
import datetime
import itertools
import operator
from statistics import mode
import collections
print (input("\nHello, Press any key to begin!"))


url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_path = "476.txt"
#response = str(urllib.request.urlopen(url).read())

if not os.path.isfile(local_path):
    # go get it
    urlretrieve(url, local_path)

file = open(local_path) 



Jan = list()
Feb = list()
Mar = list()
Apr = list()
May = list()
Jun = list()
Jul = list()
Aug = list()
Sep = list()
Oct = list()
Nov = list()
Nov = list()
Dec = list()

days = list()

TOTAL_REQS = 0
pattern = re.compile(r'[0-9][0-9]\W[A-Z][a-z][a-z]\W[0-9][0-9[0-9][0-9][0-9]')

fail = re.compile(r'\s[4][0-9][0-9] ')
S = re.compile(r'\s[3][0-9][0-9] ')
f = re.compile(r'GET(.*?)HTTP')

US = 0
reqs = list()
SS = 0





for line in file:
    
    for x in re.findall(f, line):
        reqs.append(x)       
    
    for x in re.findall(pattern, line):
        days.append(x)   
    
    for i in re.findall(fail, line):
        US +=1    
          
        
    for t in re.findall(S, line):
        SS +=1   
    
    if "Jan" in line:
        Jan.append(line)
    if 'Feb' in line:
        Feb.append(line)
    if 'Mar' in line:
        Mar.append(line)  
    if 'Apr' in line:
        Apr.append(line)  
    if 'May' in line:
        May.append(line) 
    if 'Jun' in line:
        Jun.append(line)  
    if 'Jul' in line:
        Jul.append(line)  
    if 'Aug' in line:
        Aug.append(line)
    if 'Sep' in line:
        Sep.append(line)  
    if 'Oct' in line:
        Oct.append(line)
    if 'Nov' in line:
        Nov.append(line) 
    if 'Dec' in line:
        Dec.append(line)     
            
    TOTAL_REQS +=1

individual_days = set(days)    

daydict = {}

for eachday in individual_days:
    count = 0
    x = eachday
    for i in days:
        if i == x:
            count =count+1
        daydict [x] = [count]

Jan = len(Jan)
Feb = len(Feb)
Mar = len(Mar)
Apr = len(Apr)
May = len(May)
Jun = len(Jun)
Jul = len(Jul)
Aug = len(Aug)
Sep = len(Sep)
Oct = len(Oct)
Nov = len(Nov)
Dec = len(Dec)       

month = {"January":Jan,"February":Feb,"March":Mar,"April":Apr,"May":May, "Jun":Jun, "Jul":Jul, "Aug": Aug, "Sep": Sep, "Oct": Oct, "Oct": Oct, "Nov": Nov, "Dec": Dec}



print ("\n1.How many total requests were made in the time period represented in the log?")
print (" ")
print (TOTAL_REQS)

print ("\n2.How many requests were made on each day? per week? per month?")
print ("\nDays:")
for a, b in daydict.items():
    print(a, b)


print ("\nMonths:")
print (" ")
for x, y in month.items():
    print(x, y)


print ("\n3.What percentage of the requests were not successful (any 4xx status code)?")
     
percent = US/TOTAL_REQS
print(" ")
print (round(percent*100,2),"%")

#Number4
print("\n4.What percentage of the requests were redirected elsewhere (any 3xx codes)?")


percents = SS/TOTAL_REQS
print(" ")
print (round(percents*100,2),"%")



#Number5


new = collections.Counter(reqs).most_common()

print("\n5.What was the most-requested file?")
print (" ")
print (new[0])

#Number6

print("\n6.What was the least-requested file?")

print (" ")


print (new[-1])

print ("\nDone!")

file.close() 