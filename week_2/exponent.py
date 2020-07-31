#exponent.py
#

def raise_to_power(base,power):
    ans = 1
    for i in range(power):
        ans *= base 
    return ans

print(raise_to_power(2,3))