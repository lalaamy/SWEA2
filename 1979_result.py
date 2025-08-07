T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())

    arr= [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N) :
        count = 0
        for j in range(N) :
            if arr[i][j] == 1 :
                count += 1
            else : 
                if count == K :
                    result += 1
                count = 0

        if count == K :
            result += 1
    
    for j in range(N) :
        count = 0 
        for i in range(N) :
            if arr[i][j] == 1 :
                count += 1
            else : 
                if count == K :
                    result += 1
                count = 0

        if count == K :
            result += 1

    print (f'#{t} {result}')