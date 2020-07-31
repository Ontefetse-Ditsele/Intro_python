#Ontefetse Ditsele
#
#13 May 2020

secret_number = 42 #create a secret number in the program
guess = 0          #variable to store user's guess

#As long as we have not found the secret number
while guess != secret_number:
  #get a new guess from user
  guess = eval(input("what is the secret number? "))
  
  #check if guess is too low
  if guess < secret_number:
    print("That is way too low please try again")
  
  #check if guess is too high
  elif guess > secret_number:
    
    print("That is way too high please try again")
    
print("Congragulations, you have guessed the secret number!")
