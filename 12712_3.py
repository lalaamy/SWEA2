plus_dr = [-1, 1, 0, 0]
plus_dc = [0, 0, -1, 1]

cross_dr = [1, 1, -1, -1]
cross_dc = [-1, 1, -1, 1]

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for r in range(N):
        for c in range(N) :

            #plus
            plus_kill = arr[r][c]
            for d in range(4):
                for m in range(1, M) :
                    nr = r + plus_dr[d]*m
                    nc = c + plus_dc[d]*m

                    if 0<= nr < N and 0 <= nc < N :
                        plus_kill += arr[nr][nc]

            # cross
            cross_kill = arr[r][c]
            for d in range(4):
                for m in range(1, M) :
                    nr = r + cross_dr[d]*m
                    nc = c + cross_dc[d]*m

                    if 0<= nr < N and 0 <= nc < N :
                        cross_kill += arr[nr][nc]

            result = max(result, plus_kill, cross_kill)
    
    print (f'#{t} {result}')