T = int(input())

for t in range(1, T+1) :
    N = int(input())
    switch = list(map(int, input().split()))
    main = list(map(int, input().split()))

    count = 0
    for i in range(len(switch)) :
        if switch[i] == main[i] :
            continue
        else :
            count += 1
            for j in range(i, N):
                if switch[j] == 0 :
                    switch[j] = 1
                elif switch[j] == 1 :
                    switch[j] = 0
        
    print (f'#{t} {count}')