T = int(input())

for t in range (1, T+1) :
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for m in range (M) :
        i, j = map(int, input().split())

        stand = arr[i]

        for plus in range(j) :
            plus_under = arr[i-j]
            plus_over = arr[i+j]

            if plus_under == plus_over :
                if plus_under == 1 :
                    plus_under = plus_over = 0
                else :
                    plus_under = plus_over = 1
            else :
                pass

    print (f'#{t} {arr}')