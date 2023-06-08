# 첫수를 입력하시오 5
# 끝수를 입력하시오 7
# 5에서 7까지 합은 18입니다.

start = input("첫수를 입력하시오 ==> ")
end = input("끝수를 입력하시오 ==> ")

arr = list(range(int(start),int(end)+1))

sum = 0

for i in arr:
    sum += i
    
print(start + "에서 " + end + "까지 합은 " + str(sum) + "입니다.")
print("{}에서 {}까지 합은 {}입니다.".format(start, end, sum))
