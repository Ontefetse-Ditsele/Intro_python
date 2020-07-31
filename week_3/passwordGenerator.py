#Ontefetse Ditsele
#
#19 May 2020

from random import choice as choose
def passwordGenerator():
    lowerchar = ['a','b','c','d','e']
    upperchar = ['F','G','H','I','J']
    spcl_char = ['&','@','!','£','$']
    numb_char = ['1','2','3','4','5']

    password = choose(lowerchar) + choose(upperchar) + choose(spcl_char) + choose(numb_char)
    password += password

    return password

print(passwordGenerator())
print(passwordGenerator())
print(passwordGenerator())
