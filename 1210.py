

# di = [-1, 0, 0] # 상 좌 우 (위로만 갈 거고 0이면 안 갈 거임)
# dj = [0, -1, 1]


for t in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited_arr = [[0]*100 for _ in range(100)]

    for j in range (100) :
        if arr[99][j] == 2 : # start / i ==99
            now_i, now_j = 99, j

    while now_i != 0 :
        visited_arr[now_i][now_j] = 1
        
        # 좌로 이동
        if 0 <= now_j -1 < 100 :
            if arr[now_i][now_j-1] == 1 and visited_arr[now_i][now_j-1] == 0 :
                now_j -= 1
                continue

    
        # 우로 이동 
        if 0 <= now_j + 1 < 100 :
            if arr[now_i][now_j+1] == 1 and visited_arr[now_i][now_j+1] == 0 :
                now_j += 1
                continue

        # 위로 이동
        if 0 <= now_i-1 < 100 :
            if arr[now_i-1][now_j] == 1 and visited_arr[now_i-1][now_j] == 0 :
                now_i -= 1
                continue

    print (f'#{t} {now_j}')


## 강사님 풀이

dr = [-1, 0, 0]
dc = [0, -1, 1]

search_dir = [[1,2,0], [0,1], [0,2]]
# 위를 볼 때는 왼쪽, 오른쪽 보고 위를 보기
# 왼쪽을 볼 때는 

T = 10
for t in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    c = ladder[99].index(2)

    dir = 0
    while r > 0 :

        for i in range(len(search_dir[dir])):
            # 다음 방향이 가능한 거 보기
            next_dir = search_dir[dir][i]
            next_r = r + dr[next_dir]
            next_c = c + dc[next_dir]
        
            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break
            
    print (f'#{t} {c}')