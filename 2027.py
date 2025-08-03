# 대각선 출력

lst = []
for i in range(5) :
    for j in range(5) :
        if i == j:
            lst1 = lst.append('#')
        else :
            lst2 = lst.append('+')
    print (lst1 + lst2)