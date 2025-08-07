T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())

    arr= [list(map(int, input().split())) for _ in range(N)]

    j_count = 0
    for i in range (N) :
        for j in range(N-K+1):
            K_i = (arr[i][x] for x in range (j, j+K))
            # K_i = arr[i][j : j+K]
            # if arr[i][j : j+K] == [1]*K :
            if K_i == [1]*K :
            
            # if sum(K_i) == K :
                # if arr[i][j+K+1] != 1 or  (K_i in arr):
                if (j == 0 or arr[i][j-1] == 0) and (j+K == N or arr[i][j+K] == 0) :
                    j_count += 1
                continue
    
    i_count = 0
    for j in range(N) :
        for i in range(N-K+1) :
            # K_j = arr[i : i+K][j]
            K_j = (arr[x][j] for x in range (i, i+K))
            # if arr[i : i+K][j] == [1]*K :
            if K_j == [1]*K :
            
            # if sum(K_j) == K :
                # if arr[i+K+1][j] != 1  or  (K_j in arr) :
                if (i == 0 or arr[i-1][j] == 0) and  (i+K == N or arr[i+K][j] == 0) :
                    i_count += 1
                continue
    
    print (f'#{t} {i_count+j_count}')




T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())

    arr= [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range (N) :
        count = 0
        for j in range(N-K+1):
            K_i = (arr[i][x] for x in range (j, j+K))
            if K_i == [1]*K :
                if (j == 0 or arr[i][j-1] == 0) and (j+K == N or arr[i][j+K] == 0) :
                    count += 1
                
        if count == K :
            result += 1
    
    for j in range(N) :
        count = 0
        for i in range(N-K+1) :
            K_j = (arr[x][j] for x in range (i, i+K))
            if K_j == [1]*K :
                if (i == 0 or arr[i-1][j] == 0) and  (i+K == N or arr[i+K][j] == 0) :
                    count += 1
        if count == K :
            result += 1       
    
    print (f'#{t} {count}')