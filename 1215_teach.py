for t in range(1, 11) :
    N = int(input())
    graph = [input() for _ in range(8)]
    answer = 0

    for i in range(8) :
        for j in range(8-N+1) :

            for k in range(N//2) :
                if graph[i][j+k] != graph[i][j+N-1-k] :
                    break
            else : 
                answer += 1

            for k in range(N//2) :
                if graph[j+k][i] != graph[j+N-1-k][i] :
                    break
            else : 
                answer += 1
    
    print (f'#{t} {answer}')