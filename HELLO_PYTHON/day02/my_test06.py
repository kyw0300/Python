# 가위/바위/보를 선택하세요
# 나 : 가위
# 컴 : 바위
# 결과 : 패배
from random import random

me = input("가위/바위/보를 선택하세요 ==> ")
# print(me)

rsp = ["가위","바위","보"]

rancom = int(random()*3)
com = rsp[rancom]

print("나 : " + me)
print("컴 : " + com)

if me == com:
    res = "무승부!"
elif (me=="바위" and com=="가위") or (me=="가위" and com=="보") or (me=="보" and com=="바위") :
    res = "승리!"
else:
    res = "패배!"
    
print("결과 : " + res)