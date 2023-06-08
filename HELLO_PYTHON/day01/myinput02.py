# 숫자를 입력하시오
# 또 숫자를 입력하시오
# 5와 6의 합은 11입니다.

a = input("숫자를 입력하시오 ==> ")
b = input("또 숫자를 입력하시오 ==> ")
sum = int(a)+int(b)

print(a + "와 " + b + "의 합은 " + str(sum) + "입니다.")
print("{}와 {}의 합은 {}입니다.".format(a,b,sum))