#Grid.py
#

n = int(input("Enter a start number: "))

row = "{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}"

for i in range(1,5):
    output = []
    for j in range(7):
        output.append(n)
        n += 1
    print(row.format(output[0],output[1],output[2],output[3],output[4],output[5],output[6]))
    