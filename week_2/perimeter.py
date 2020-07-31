#Ontefetse Ditsele
#
#14 May 2020


# Request values from the user.
width_one = eval(input("Enter width 1: "))
height_one= eval(input("Enter height 1: "))

width_two = eval(input("Enter width 2: "))
height_two= eval(input("Enter height 2: "))

price = eval(input("Enter price per meter: "))

#Calculate the perimeter of the shape.
perimeter = (2*width_one)+(2*width_two)+height_one+height_two+(height_one-height_two)

#Display results to user.
print("The total fence required = ",perimeter," meters")
print("The total price = ",price*perimeter)
