#Ontefetse Ditsele
#
#18 May 2020


hours = int(input("Enter the hours: \n")
)
minutes = int(input("Enter the minutes: \n"))
seconds = int(input("Enter the seconds: \n"))
if 0 <= hours < 24 and  0 <= minutes<60 and 0 <= seconds < 60:
 print("Your time is valid")
  
else:
 print("Your time is invalid")
