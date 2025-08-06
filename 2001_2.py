T = int(input())

for t in range(1, T+1) :
    N,M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for n1 in range (N-M+1):
        for n2 in range (N-M+1) :

            total = 0

            for m1 in range (M) :
                for m2 in range (M) :
                    total += arr[n1+m1][n2+m2]

            
            if max_sum <= total :
                max_sum = total
    
    print (f'#{t} {max_sum}')