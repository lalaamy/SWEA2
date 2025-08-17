    #세로 가로 우하향 우상향
dr = [1, 0, 1, 1]
dc = [0, 1, 1, -1]

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = "NO"
        
    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == "o" :
                for d in range(4):
                    count = 1
                    for m in range(1, 5) :
                        nr = r + dr[d] * m
                        nc = c + dc[d] * m
                        if 0 <= nr < N and 0 <= nc < N :
                            if arr[nr][nc] == "o" :
                                count += 1
                            else :
                                if count >= 5 :
                                    result = "YES"
                                    break
                                count = 0
                        else :
                            break
                    if count >= 5 :
                        result = "YES"
                        break
                if result == "YES" :
                    break
            if result == "YES" :
                break
    
    print (f'#{t} {result}')