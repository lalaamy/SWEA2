T = 10
for t in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))

    view = 0
    for n in range(2, N-2) :
        first_max = max(arr[n-2:n+3])
        if first_max == arr[n] :
            second_max = max(arr[n-2], arr[n-1], arr[n+1], arr[n+2])
            view += (first_max - second_max)
        else :
            continue
    
    print (f'#{t} {view}')