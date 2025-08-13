for t in range(1, 11) :
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    # arr_reverse = [''.join(row) for row in zip(*arr)]

    arr_reverse = [list(row) for row in zip(*arr)]

    result = 0

    for r in range (8):
        for c in range(8) :

            if len(arr[r][c:c+N]) == N :
                temp = arr[r][c:c+N]
                rev_temp = temp[::-1]

                if temp == rev_temp :
                    result += 1
                
    for r in range (8):
        for c in range(8) :

            if len(arr_reverse[r][c:c+N]) == N :
                now = arr_reverse[r][c:c+N]
                rev_now = now[::-1]

                if now == rev_now :
                    result += 1
    
    print (f'#{t} {result}')