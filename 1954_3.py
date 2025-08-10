T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [([0]*N) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c, d = 0, 0, 0
    num = 1

    for _ in range(N**2) :
        arr[r][c] = num
        num += 1

        nr = r + dr[d]
        nc = c + dc[d]
        
        if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc] != 0 :
            d = (d+1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
        
        r, c = nr, nc

    print (f'#{t}')

    for row in arr :
        print(*row)
