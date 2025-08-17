T =int (input())

# 방향 상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, T+1) : 
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 전체 0의 갯수 세기
    total_zero = 0
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 0 :
                total_zero += 1

            # 괴물 위치 찾기
            if arr[i][j] == 2 :
                r = i
                c = j

                # 광선으로 맞출 수 있는 0의 갯수 세기
                count = 0
                for d in range(4) :
                    for m in range(N) :
                        nr = r + dr[d] * m
                        nc = c + dc[d] * m

                        if 0 <= nr < N and 0 <= nc < N :
                            if arr[nr][nc] == 0 :
                                count += 1
                            elif arr[nr][nc] == 1 :
                                break
    
    # 괴물이 맞춘 나머지의 0 갯수 세기
    result = total_zero - count
    
    print (f'#{t}',(result))
                        