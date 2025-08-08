## 0을 만났을 때 이전의 위치를 기억한다면 차이를 이용하여 길이 파악하기

T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)] # N*N 만들기

    answer = 0

    for r in range(N) :
        recent_c = -1

        for c in range(N) :
            if graph[r][c] == 0 :
                if c - recent_c -1 == K :
                    answer += 1
                    
                recent_c = c
        
        if N - recent_c -1 == K :
            answer += 1
    
    for c in range(N) :
        recent_r = -1

        for r in range(N) :
            if graph[r][c] == 0 :
                if r - recent_r -1 == K :
                    answer += 1
                    
                recent_r = r
        
        if N - recent_r -1 == K :
            answer += 1