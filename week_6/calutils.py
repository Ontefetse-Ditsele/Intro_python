#calutils.py
#
    
def is_leap_year(year):
        """given a year returns true if its a leap year, and false otherwise"""
         #A year is a leap year if its disible by 4 or 400; but also not divisible by 100
         #e.g the year 2000 would be a leap year,
        
        if ((year%4 == 0) or (year %400 == 0) and year%100 != 0):
                return True
        else:
                return False

def month_name(number):
        """given the number of a month, returns the corresponding name. 1 is January"""
        months = ("January","February","March","April","May","June","July","August","September","October","November","December")
        return months[number-1]

def days_in_month(month_number,year):
        """given a month(in a number format) and a year returns the number of days in the month"""
        month_days = (31,28,31,30,31,30,31,31,30,31,30,31)
        
        if month_number == 2 and is_leap_year(year):
                return 29
        else:
                days = month_days[month_number-1]
                return days
        
def first_day_of_year(year):
        """given a year return the number of the day which January 1st falls. 0-Sunday, ..., 6-Saturday"""
        part1 = 1 + 5*((year-1)%4)
        part2 = 4*((year-1)%100) + 6*((year-1)%400)
        day = (part1 + part2)%7
        
        return day
        
def first_day_of_month(month_number,year):
        """given a month(in the form of a number) and (4 digit) year, return the number of the day on which the first if that month falls, 0-Sunday, ..., ^ 6-Saturday"""        
        from calendar import weekday
        return weekday(year,month_number,1) + 1
####
## MAIN FUNCTION
#####
"""   
    
while True:
        print("Choose from the following options:\n")
        print("\n0. quit\n\n1. Test is_leap_year().")
        print("\n2. Test month_name()\n\n3. Test days_in_month()")
        print("\n4. Test first_day_of_year().\n\n5. Test first_day_of_month()\n")
        
        response = int(input(""))    
        if response == 1:
                ans = int(input("Enter the year (4 digits):\n\n"))
                
                if is_leap_year(ans):
                        print("The year {} is a leap year".format(ans))
                else:
                        print("The year {} is not a leap year".format(ans))
        elif response == 2:
                for month in range(1,13):
                        print("\n\nMonth number {} is {}.".format(month,month_name(month)))
        elif response == 3:
                month_year = input("Enter month year e.g 3 2015 would be (March 2015)").split()
                mon = int(month_year[0])
                y_r = int(month_year[1])
                print(days_in_month(mon,y_r))
        
        elif response == 4:
                week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
                
                year = int(input("Enter a 4 digit year (2019): \n"))
                day = first_day_of_year(year)
                return day
                 
        elif response == 5:
                month_year = input("Enter month year e.g 3 2015 would be (March 2015)").split()
                
                return first_day_of_month(6,2020)
        else:
                break
"""