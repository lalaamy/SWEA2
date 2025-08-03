T = int(input())

for t in range(T) :
    N = list(map(int, input().split()))
    # for n in N :
    N_share = N[0] // N[1]
    N_remainder = N[0] % N[1]
    print (f'#{t+1} {N_share} {N_remainder}')
