# 1에서 9사이의 숫자 중 중복없이 3개의 숫자를 선택하세요
from random import random

rnd = (random()*9 + 1)%10
rrnd = int((random()*9 + 1)%10)

print(rnd)

set = []
j=0
while len(set)<3 :
    rrnd = int((random()*9 + 1)%10)

    for i in range(len(set)+1):
        if set[i]==rrnd:
            # j -= 1
            break
        else:
            set.append(rrnd)
            # j += 1



print(set)

# arr = [1,2,3,4,5,6,7,8,9]
#
# for i in range(99):
#     rnd = int(random()*9)
#
#     a = arr[rnd]
#     b = arr[0]
#     arr[0] = a
#     arr[rnd] = b
#
# print(arr)