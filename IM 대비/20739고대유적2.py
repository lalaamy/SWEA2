T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range (M)]

    max_count = 0
    for r in range(M) : # 행의 수
        count = 0
        for c in range(N) : # 열의 수

            if arr[r][c] == 1 :
                count += 1
            
            if arr[r][c] == 0 :
                if max_count < count :
                    max_count = count
                count = 0
        
        if max_count < count :
            max_count = count


