import datetime #importing datetime
import calendar #importing calender

def no_of_Thursdays(from_year, to_year):    # defining function to get the count of Thursdays
  from_date = "0101"+str(from_year)         # converting from year to int to string with start date
  to_date = "3112"+str(to_year)             # converting to year to int to string with end date
  from_date  = datetime.datetime.strptime(from_date, '%d%m%Y')      #Defining the date format with strptime for from date
  to_date    = datetime.datetime.strptime(to_date, '%d%m%Y')        #Defining the date format with strptime for to date
  count=0       # defining count to get no.of thursdays
  for i in range((to_date - from_date).days):       #looping through no.of days between from date and to date
    #print((from_date + datetime.timedelta(days=i+1)).weekday())        #check weekday numbers
    #print(calendar.day_name[(from_date + datetime.timedelta(days=i+1)).weekday()])         #check weekday 
    day = calendar.day_name[(from_date + datetime.timedelta(days=i+1)).weekday()]       #getting week day
    if day=="Thursday":         #checking weekday is Thursday or not
      count=count+1         #if true increment count by 1
  return count      # returning count



#print("no.of Thursday days are:"+no_of_Thursdays(1990, 2000))      #Checking with direct inputs

print("Enter start year")   # prompt user to enter start year
from_year = input()         # Reading start year
print("Enter end year")     # prompt user to enter start year
to_year = input()           # Reading end year
print("no.of Thursday days are:"+str(no_of_Thursdays(from_year, to_year)))

