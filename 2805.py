T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0

    for r in range(N) :
        start_c = abs(N//2 -r)
        count_c = N - (abs(N//2-r)*2)

        for c in range(start_c, start_c+count_c) :
            result += arr[r][c]

    
    print (f'#{t} {result}')