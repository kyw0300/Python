# 출력할 단수를 입력하시오 4
# 4 * 1 = 4
# 4 * 2 = 8 ...

gugu = input("출력할 단수를 입력하시오 ==> ")

arr = list(range(1,9+1))

print()
print("*** " + gugu + "단 ***")
for i in arr:
    print(gugu + " * " + str(i) + " = " + str(int(gugu)*i))