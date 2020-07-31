#advanced calculator
#

num1 = int(input("Enter the first number: "))
oper = input("Enter an operation: ")
num2 = int(input("Enter the second number: "))

if oper == "+":
    print(num1,"+",num2,"=",num1+num2)
elif oper == "-":
    print(num1,"-",num2,"=",num1-num2)
elif oper == "*":
    print(num1,"*",num2,"=",num1*num2)
elif oper == "/":
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid Operator")