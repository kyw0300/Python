# 홀/짝을 입력하시오 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random

rnd = random()

mine = input("홀/짝을 입력하세요 ==> ")

if rnd > 0.5:
    com = '짝'
else:
    com = '홀'

if mine == com:
    res = "승리"
else:
    res = "패배"

print('나 :',mine)
print('컴 :',com)
print('결과 :',res)

print('바보',end='\t')
print('천재')
