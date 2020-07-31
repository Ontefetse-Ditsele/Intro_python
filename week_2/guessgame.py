#Ontefetse Ditsele
#
#13 May 2020

secret_word = "Giraffe"
guess = ""

guess_count = 0
guess_limit = 3

out_of_guess = False

while guess != secret_word and not out_of_guess:
  if guess_count < guess_limit:
    guess = input("Enter a guess: ")
    guess_count += 1
  else:
    out_of_guess = True
if out_of_guess:
  print("You are out of guess,You Lose ")
else:
  print("Congrats, You win")
