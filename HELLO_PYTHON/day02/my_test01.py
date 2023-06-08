# range를 이용하여 1에서 10까지 합을 구하시오

sum = 0
arr = list(range(1,10+1))

for i in arr :
    sum += i

print(arr)
print("1부터 10까지 합 :",sum)