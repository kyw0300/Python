arr = ["홍길동","전우치","이순신"]

arr.append("유관순")
arr.insert(4, "윤봉길")
arr.insert(len(arr), "윤봉길") # len(arr)을 이용하면 append와 같은 효과

print(arr)
print(len(arr))
