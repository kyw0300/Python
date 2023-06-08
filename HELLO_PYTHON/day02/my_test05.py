# 첫수를 입력하시오 1
# 끝수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지의 5의 배수의 합은 15입니다.

start = input("첫 수를 입력하시오 ==> ")
end = input("끝 수를 입력하시오 ==> ")
num = input("배수를 입력하시오 ==> ")
inum = int(num)

arr = list(range(int(start),int(end)+1))
# print(arr)

sum = 0

for i in arr:
    if i%inum == 0:
        sum += i

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(start,end,num,sum))