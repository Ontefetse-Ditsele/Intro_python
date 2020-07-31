month = input("Enter the month(January,...,December):\n")
dayone = input("Enter the day(Monday,...,Sunday): \n")


months = ["January","March","May","July","August","October","December"]
row = "{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}"

print("Mo Tu We Th Fr Sa Su")
if dayone == "Sunday":
    print(row.format(" "," "," "," "," "," ",1))
    n = 2
else:
    n=1
for i in range(4):
    output = []
    for j in range(7):
        output.append(n)
        n += 1
    print(row.format(output[0],output[1],output[2],output[3],output[4],output[5],output[6]))
