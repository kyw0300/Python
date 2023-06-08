def gugu(dan):
    result = ""
    
    for i in range(1,9+1):
        if i != 5:
            result += str(dan) + " * " + str(i) + " = " + str(dan*i) + "\n"
    result += "\n"
    
    return result

ret = ""
for j in range(9,2-1,-1):
    if j==9 or j==7 or j==3 or j==2:
        ret += gugu(j)
    
print(ret)

#메소드의 중요성!
#for문을 최소화하자!
    