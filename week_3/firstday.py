#Ontefetse Ditsele
#
#20 May 2020

week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

year_one = int(input("Enter the first year:\n"))
year_two = int(input("Enter the second year:\n"))

for index in range(year_one,year_two+1,1):
  #Separate the formula into two parts and add them together
  part1 = 1 + 5*((index-1)%4)
  part2 = 4*((index-1)%100) + 6*((index-1)%400)
  day = (part1 + part2)%7
  
  #Display answer to the user for each iteration
  print("The first of January",index,"Falls on a ",week[day])
