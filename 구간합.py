T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))

    N_sum = []

    for n in range(N-M+1) :
        N_part = N_arr[n:n+M]
        N_sum.append(sum(N_part))

    result = max(N_sum) - min(N_sum)

    print (f'#{t} {result}')