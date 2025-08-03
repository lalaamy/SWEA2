def calcul(a, b) :
    print (a+b)
    print (abs(a-b))
    print (a*b)
    print (a//b)

A, B = map(int, input().split())
calcul(A, B)