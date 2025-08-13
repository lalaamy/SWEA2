T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range (N)]
    
    total_count = 0
    for r in range(N) :
        count = 0
        for c in range(N) :
            
            if arr[r][c] == 1 :
                count += 1
                continue
            elif arr[r][c] == 0 :
                if count == M :
                    total_count += 1
                count = 0
        if count == M :
            total_count += 1

    for c in range(N) :
        count = 0
        for r in range(N) :
            
            if arr[r][c] == 1 :
                count += 1
                continue
            elif arr[r][c] == 0 :
                if count == M :
                    total_count += 1
                count = 0
        if count == M :
            total_count += 1
    

    print (f'#{t} {total_count}')