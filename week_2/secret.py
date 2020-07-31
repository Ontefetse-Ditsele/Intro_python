#Ontefetse Ditsele
#
#14 May 2020

secret_number = 42
guess = 0

while guess != secret_number:
  guess = eval(input("?"))
  
  if guess < secret_number:
    print("lo")
  
  elif guess > secret_number:
    print("hi")

print("Correct")
