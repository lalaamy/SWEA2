T = int(input())

for t in range(1, T+1) :
    N = int(input())
    A_switches = list(map(int, input().split()))
    B_switches = list(map(int, input().split()))

    count = 0
    for i in range(len(A_switches)) :
        if A_switches[i] == B_switches[i] :
            continue
        else :
            for j in range(i, len(A_switches)) :
                A_switches[j] = 1 - A_switches[j]
            count += 1
        
    print (f'#{t} {count}')