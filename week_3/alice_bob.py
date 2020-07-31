#Ontefetse Ditsele
#
#20 May 2020

a = list(map(int,input().split()))
b = list(map(int,input().split()))

#alice_score = 0
#bob_score = 0
#for index in range(3):
#  if a[index] > b[index]:
#    alice_score += 1
#  if a[index] < b[index]:
#    bob_score += 1

alice_score = sum([(1 if a[i]>b[i] else 0) for i in range(3)])
bob_score = sum([(1 if a[i] < b[i] else 0) for i in range(3)])

print(alice_score,bob_score)
