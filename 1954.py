T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, d = 0, 0, 0
    num = 1

    for _ in range (N*N) :
        arr[x][y] = num
        num += 1

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] != 0 :
            # 방향 전환
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x, y = nx, ny
    
    print(f'#{t}')
    for row in arr :
        print(*row)