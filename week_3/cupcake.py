#Ontefetse Ditsele
#
#19 May 2020

print("Welcome to the 30 second expect rule game--------------------")
print("Answer the following questions by selection from among the options")

ans = input("Did anyone see you(yes/no)\n")
if ans == "yes":
  ans = input("Was it a boss/lover/parent?(yes/no)\n")
  if ans == "no":
    print("Eat It")
  else:
    ans = input("Was it expensive(yes/no)\n")
    if ans == "yes":
      ans = input("Can you cut of the part that touched the floor?(yes/no): \n")
      if ans == "yes":
        print("Eat it")
      else:
        print("Your call")
    else:
      ans = input("is it chocolate?(yes/no)\n")
      if ans == "yes":
        print("Eat it")
      else:
        print("Don't eat it")
else:
  ans = input("Was it sticky?(yes/no)\n")
  if ans == "yes":
    ans = input("Is it a raw steak?(yes/no)\n")
    if ans == "yes":
      ans = input("Are you a puma?(yes/no)\n")
      if ans == "yes":
        print("Eat it")
      else:
        print("Don't eat it")
    else:
      ans = input("Did the cat lick it?(yes/no)\n")
      if ans == "no":
        print("Eat it")
      else:
        ans = input("Is it a healthy cat?(yes/no)\n")
        if ans == "yes":
          print("Eat it")
        else:
          print("Your call")
  else:
    ans = input("Is it an emausaurus(yes/no)\n")
    if ans == "yes":
      ans = input("Are you a megalosaurus(yes/no)\n")
      if ans == "yes":
        print("Eat it")
      else:
        print("Don't eat it")
    else:
      ans = input("Did the cat lick it?(yes/no)\n")
      if ans == "no":
        print("Eat it")
      else:
        ans = input("Is your cat healthy?(yes/no)\n")
        if ans == "yes":
          print("Eat it")
        else:
          print("Your call")
