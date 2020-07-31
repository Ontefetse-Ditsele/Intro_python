#vectormath
#
from math import sqrt

v_A = input("Enter vector A:\n").split()
v_B = input("Enter vector B:\n").split()

v_a = list(map(int,v_A))
v_b = list(map(int,v_B))

total_add = []
for i in range(3):
    ans = v_a[i] + v_b[i]
    total_add.append(ans)
    
dot_v = (v_a[0] * v_b[0]) + (v_a[1] * v_b[1]) + (v_a[2] * v_b[2])
    
norm_a = sqrt((v_a[0]**2) + (v_a[1]**2) + (v_a[2]**2))
norm_b = sqrt((v_b[0]**2) + (v_b[1]**2) + (v_b[2]**2))

print("A+B  =",total_add)
print("A.B  =",dot_v)
print("|A|  = {:.2f}".format(norm_a,2))
print("|B|  = {:.2f}".format(norm_b,2))
