#Ontefetse Ditsele
#
#21 May 2020

from math import sqrt

denominator = sqrt(2)
next_term = 2/denominator

pi = 2 * 2/denominator

while next_term > 1:
  denominator = sqrt(2 + denominator)
  next_term = 2/denominator
  pi *= next_term

print("Approximation of PI is",round(pi,3))
radius = float(input("Enter the radius:\n"))
print("Area:",round(pi * (radius**2),3))
