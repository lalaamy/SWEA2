def dfs(node) :
    global answer
    if node == 99 :
        answer = 1
        return
    
    for next_node in adj_list[node] :
        if visited[next_node] :  # 1일 때 True (0이 아니면 True)
            continue

        visited[next_node] = 1
        dfs(next_node)
        visited[next_node] = 0

for t in range(1, 11) :
    T, M = map(int, input().split())
    info = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    visited = [0] * 100

    answer = 0
    for i in range(M) :
        # if i % 2 == 0 :
        #     temp = info[i]
        
        # elif i % 2 == 1 :
        #     adj_list[temp].append(info[i])

        a = info[2*i]
        b = info[2*i+1]
        adj_list[a].append(b)

    visited[0] = 1
    dfs(0)
    visited[0] = 0

    print (f'#{t} {answer}')