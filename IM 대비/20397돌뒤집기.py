T = int(input())

for t in range (1, T+1) :
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for m in range (M) :
        i, j = map(int, input().split())

        stand = i - 1

        for plus in range(1, j+1) :
            plus_under = i-1 -plus
            plus_over = i-1 +plus

            if 0 <= plus_under < N and 0 <= plus_over < N :
                if arr[plus_under] == arr[plus_over] :
                    if arr[plus_under] == 1 :
                        arr[plus_under] = arr[plus_over] = 0
                    else :
                        arr[plus_under] = arr[plus_over] = 1
                else :
                    pass

    print (f'#{t}', end=' ')
    for row in arr :
        print (row, end= " ")
    print()