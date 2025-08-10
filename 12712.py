T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # + 모양 방향 델타 (상, 하, 좌, 우)
    plus_dr = [-1, 1, 0, 0]
    plus_dc = [0, 0, -1, 1]

    # x 모양 방향 델타 (오른쪽 위, 오른쪽 아래, 왼쪽 아래, 왼쪽 위)
    cross_dr = [-1, 1, 1, -1]
    cross_dc = [1, 1, -1, -1]

    # 중심 지점 순회
    for r in range(N) :
        for c in range(N) :
            
            #델타 순회 ; + 방향
            kill_plus = arr[r][c]
            for d in range(4) :
                # 분무 범위
                for m in range(1, M) :
                    nr = r + (plus_dr[d]*m)
                    nc = c + (plus_dc[d]*m)

                    if 0 <= nr < N and 0 <= nc < N :
                        kill_plus += arr[nr][nc]

            #델타 순회 ; X 방향
            kill_cross = arr[r][c]
            for d in range(4) :
                for m in range(1, M) :
                    nr = r + (cross_dr[d] * m)
                    nc = c + (cross_dc[d] * m)

                    if 0<= nr < N and 0 <= nc < N :
                        kill_cross += arr[nr][nc]
    
            result = max(result, kill_cross, kill_plus)

    print (f'#{t} {result}')