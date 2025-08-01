T = int(input())

for t in range(T) :
    N = list(map(int, input().split()))
    N_max = 0
    for n in range(len(N)) :
        if N[n] > N_max :
            N_max = N[n]
        else :
            continue
    print (f'#{t+1} {N_max}')