T = int(input())

for t in range(1, T+1) :
    n, m =map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_fly = 0

    for r in range(n-m+1) :
        for c in range(n-m+1) :

            fly_sum = 0

            for p in range(m) :
                for q in range(m) :
                    fly_sum += arr[r+p][c+q]
            
            if max_fly <= fly_sum :
                max_fly = fly_sum
            
    print (f'#{t} {max_fly}')