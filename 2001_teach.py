T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    answer = 0 # 파리 최솟값

    for i in range(N-M+1) : # 시작점 확정
        for j in range(N-M+1) :

            temp_sum = 0

            for p in range(M) : 
                for q in range(M) : 
                    temp_sum += flies [i+p][j+q]

            if answer < temp_sum: # 파리채 다 돌고 answer 해야 하니까
                answer = temp_sum