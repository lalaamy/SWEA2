T = int(input())
 
for t in range(1, T+1) :
    N = int(input())
    arr = [(list(map(int, input().split()))) for _ in range (N)]
 
 
    max_sum = 0
    for r in range (N) :
        for c in range (N) :
            total_sum = -(arr[r][c])
 
            for i in range(N) :
                total_sum += arr[r][i]
             
            for j in range(N) :
                total_sum += arr[j][c]
 
            if max_sum < total_sum :
                max_sum = total_sum
 
     
    print (f'#{t} {max_sum}')