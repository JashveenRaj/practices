# common birthday dates spotting program

# basics : april , june ,sept , nov = 30 days
#        : january march may july aug oct dec = 31 days
#        : febrauary = 28 or 29 days

# logic for feb : if given yr is divisible by 4 = leap year
#               : if given year is a century year (1800,1900,,,divisible by 100) then it is a leap year only if divisible by 400
#               : if year is divisible by 100 = not leap year

# month wise logic:
#If month is February and year is leap year then
#Generate day randomly from 1 to 29
#If month is February and year is not a leap year then
#Generate day randomly from 1 to 28
#If month%2==0 and month<7 then // April (4) and June(6)
#Generate day randomly from 1 to 30
#If month%2==0 and month>7 then // August(8), October(10) and December(12)
#Generate day randomly from 1 to 31
#If month%2!=0 and month<=7_then // January(1), March(3), May(5), July(7)
#Generate day randomly from 1 to 31
#If month%2!= 0 and month>7 then // September(9) and November(11)
#Generate day randomly from 1 to 30

#PROGRAM TO GENERATE RANDOM DATES OR DAYS FROM AN YEAR


import random
import datetime

birthday = []
i = 0
while i < 50:
    year = random.randint(1850, 2023)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1
    else:
        leap = 0

    month = random.randint(1, 12)

    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30) # generate randome date out of 30 for these months
    elif month == 2:
        if leap:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28) # for february
    else:
        day = random.randint(1, 31) # for rest of the months
 
    try:
        date = datetime.date(year, month, day) #format we want to use
        day_of_the_year = date.timetuple().tm_yday # function to covert the date of a particular month to a day in year (out of 365)
        birthday.append(day_of_the_year)
        i = i + 1
    except ValueError:
        # Handle the case when the day is out of range for the selected month
        pass

birthday.sort()
i = 0
while i < 50:
    print(birthday[i])
    i = i + 1

