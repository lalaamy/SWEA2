import math

T = int(input())

for t in range(T) :
    N = int(input())
    arr = ""
    for i in range(N) :

        Ci, Ki = input().split()
        Ki = int(Ki)

        arr += Ci * Ki

    print(f'#{T}')

    for j in range ((len(arr)//10)+1) :
        if j >= (len(arr)//10) :
            print(arr [j*10:])
        else :
            print(arr [j*10 : j*10+10])




    # for j in range((len(arr) // 10)+1) : 
    #     if j == len(arr) // 10 :
    #         print (*arr [i*10:], sep="")
    #     else :
    #         print (*arr [i*10:i*10+10], sep="")



