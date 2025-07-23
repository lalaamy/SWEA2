# print("#++++ \n+#+++ \n++#++ \n+++#+ \n++++#")

# 내 풀이
sharp = "#"
plus = "+"
for i in range(5) :
    sharp_plus = i * plus + sharp + (4 - i) * plus
    print(sharp_plus)

# for i in range(5) :
#     arr = ["+", "+", "+", "+", "+"]
#     arr[i] = "#"
#     print(*arr, sep = "")

# 강사님 풀이
for i in range(5):
    for j in range(5):
        if i == j :
            print("#", end = "")
        else :
            print("+", end = "")
    print()

# 또 다른 풀이
for i in range(5) :
    temp = ["+"] * 5
    temp[i] = "#"

    temp = "".join(temp) #str에 join 함수를 이용해서 스트링을 합치는 것 권유
    print(temp)