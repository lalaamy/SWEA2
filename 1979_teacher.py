T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)] # N*N 만들기

    answer = 0

    for r in range(N) :
        count = 0
        for c in range(N) :
            if graph[r][c] == 1 :
                count += 1
                continue   # else 안 쓰는 조건  

            if count == K :    # 자동 else 구문
                answer += 1
            count = 0

        if count == K :
            answer += 1


    for c in range(N) :
        count = 0
        for r in range(N) :
            if graph[r][c] == 1 :
                count += 1
                continue   # else 안 쓰는 조건  

            if count == K :    # 자동 else 구문
                answer += 1
            count = 0
            
        if count == K :
            answer += 1