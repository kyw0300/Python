from random import random
arr=[]
for i in range(1,45+1):
    arr.append(i)
# print(arr)

for i in range(99):
    rnd = int(random()*45)

    a = arr[rnd]
    b = arr[0]
    arr[0] = a
    arr[rnd] = b

print(arr[:6])