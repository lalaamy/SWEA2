""" 
가위는 1
바위는 2
보는 3

가위 1 < 바위 2
바위 2 < 보 3
보 3 < 가위 1
"""

A, B = list(map(int, input().split()))

if A == 1 :
    if B == 2 :
        print ("B")
    else :
        print ("A")
elif A == 2 :
    if B == 1 :
        print ("A")
    else :
        print ("B")
else :
    if B == 2 :
        print ("A")
    else :
        print ("B")