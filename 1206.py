for t in range(1, 11) :
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range (2, N-2) :
        if max(arr[i-2:i+3]) == arr[i] :
            first_max = arr[i]
            second_max = max([arr[i-2], arr[i-1], arr[i+1], arr[i+2]])
            result += (first_max - second_max)
    print (f'#{t} {result}')