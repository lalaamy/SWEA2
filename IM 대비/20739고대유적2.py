T = int(input())

for t in range(1, T+1) :
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range (M)]
    
    r_max_count = 0
    for r in range(M) : # 행의 수
        count = 0
        for c in range(N) : # 열의 수
            
                if arr[r][c] == 1 :
                    count += 1
                
                if arr[r][c] == 0 :
                    if r_max_count < count and count > 1:
                        r_max_count = count
                    count = 0
        
        if r_max_count < count and count > 1 :
            r_max_count = count


    c_max_count = 0
    for c in range(N) : # 열의 수
        count = 0
        for r in range(M) : # 행의 수

            if arr[r][c] == 1 :
                count += 1
                
            
            if arr[r][c] == 0 :
                if c_max_count < count and count > 1 :
                    c_max_count = count
                count = 0
        
        if c_max_count < count and count > 1:
            c_max_count = count

    total_max = max(r_max_count, c_max_count)
    print (f'#{t} {total_max}')

