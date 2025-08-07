

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
