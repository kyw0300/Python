def showDan(dan):
    # pass
    print(str(dan) + "단")
    
    for i in range(1,9+1):
        print(str(dan) + " * " + str(i) + " = " + str(dan*i))

dan = int(input("출력할 구구단 단을 입력하세요 ==> "))
showDan(dan)