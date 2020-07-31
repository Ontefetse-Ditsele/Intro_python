#Ontefetse Ditsele
#
#19 May 2020

from math import sqrt as sqrt

side_a = eval(input("Enter the length of the first side: "))
side_b = eval(input("Enter the length of the second side: "))
side_c = eval(input("Enter the length of the third side: "))

length_s = (side_a+side_b+side_c)/2
area = length_s*(length_s-side_a)*(length_s-side_b)*(length_s-side_c)

print("The area of the triangle with sides of length",side_a,"and",side_b,"and",side_c,"is",sqrt(area))
