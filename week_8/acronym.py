#Ontefetse Ditsele
#
#18 June 2020
                                                                #revomes the spaces
ignore = input("Enter words to be ignored separated by commas:").replace(" ","").lower()
ignore = ignore.split(",")

title = input("Enter a title to generate its acronym:\n").lower().split()
acronym = ""

for word in title:
  if not (word in ignore):
    acronym += word[0]

print("The acronym is :", acronym.upper())