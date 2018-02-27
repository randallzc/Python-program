import urllib.request
import urllib.parse
import re
import datetime
import itertools
import operator

print (input("\nHello, Press any key to begin!"))

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
response = str(urllib.request.urlopen(url).read())

file = open("adam.txt","w") 
file.write(response)


#Number 1
total= ()
total = re.findall(r' - - ', response)

print ("\n1.How many total requests were made in the time period represented in the log?")
print (" ")
print (len(total))



#Number 2
month_Jan = re.findall(r'Jan',response)
month_Feb = re.findall(r'Feb',response)
month_Mar = re.findall(r'Mar',response)
month_Apr = re.findall(r'Apr',response)
month_May = re.findall(r'May',response)
month_Jun = re.findall(r'Jun',response)
month_Jul = re.findall(r'Jul',response)
month_Aug = re.findall(r'Aug',response)
month_Sep = re.findall(r'Sep',response)
month_Oct = re.findall(r'Oct',response)
month_Nov = re.findall(r'Nov',response)
month_Dec = re.findall(r'Dec',response)

Jan = len(month_Jan)
Feb = len(month_Feb)
Mar = len(month_Mar)
Apr = len(month_Apr)
May = len(month_May)
Jun = len(month_Jun)
Jul = len(month_Jul)
Aug = len(month_Aug)
Sep = len(month_Sep)
Oct = len(month_Oct)
Nov = len(month_Nov)
Dec = len(month_Dec)

month = {"January":Jan,"February":Feb,"March":Mar,"April":Apr,"May":May, "Jun":Jun, "Jul":Jul, "Aug": Aug, "Sep": Sep, "Oct": Oct, "Oct": Oct, "Nov": Nov, "Dec": Dec}

days = ()
days = re.findall(r'[0-9][0-9]\W[A-Z][a-z][a-z]\W[0-9][0-9[0-9][0-9][0-9]', response)

individual_days = set(days)

day = len(individual_days)

daydict = {}

for eachday in individual_days:
    count = 0
    x = eachday
    for i in days:
        if i == x:
            count =count+1
        daydict [x] = [count]


    
    
    



print ("\n2.How many requests were made on each day? per week? per month?")
print ("\nDays:")
for a, b in daydict.items():
    print(a, b)


'''print (week)'''
print ("\nMonths:")
print (" ")
for x, y in month.items():
    print(x, y)




#Number3
print ("\n3.What percentage of the requests were not successful (any 4xx status code)?")

US = re.findall(r'\s[4][0-9][0-9] ', response)

percent = len(US)/len(total)
print(" ")
print (round(percent*100,2),"%")


#Number4
print("\n4.What percentage of the requests were redirected elsewhere (any 3xx codes)?")


S = re.findall(r'\s[3][0-9][0-9] ', response)

percents = len(S)/len(total)
print(" ")
print (round(percents*100,2),"%")

#Number5

print("\n5.What was the most-requested file?")

reqs = re.findall(r'GET(.*?)HTTP ', response)

print (max(set(reqs), key=reqs.count))


#Number6

print("\n6.What was the least-requested file?")

print (min(set(reqs), key=reqs.count))



file.close() 