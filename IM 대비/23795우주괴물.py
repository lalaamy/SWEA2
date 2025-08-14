T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_count = 0
    for r in range(N) :
         for c in range(N) :
            if arr[r][c] == 0 :
                total_count += 1
    
    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 2 :
                monster_r = r
                monster_c = c
            
            # for d in range(4) :
            #     nr = r + dr[d]
            #     nc = c + dc[d]

            # if 0 <= nr < N and 0 <= nc < N :  
            count = 0
            for i in range (N) :
                c_count = 0
                for j in range(N) :
                    if arr[r][j] == 0 :
                        c_count += 1
                    elif arr[r][j] != 0 :
                        if c_count != 0 :
                            count += c_count
                        break
            
            for j in range (N) :
                r_count = 0
                for i in range(N) :
                    if arr[r][j] == 0 :
                        r_count += 1
                    elif arr[r][j] != 0 :
                        if r_count != 0 :
                            count += r_count
                        break
            result = total_count - count
    print (f'#{t} {result}')