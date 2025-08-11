T = int(input())

for t in range (1, T+1) :
    N = int(input())

    arr =list(map(int, input()))

    max_count = 0
    count = 0

    for i in range(N) :
        if arr[i] == 1 :
            count += 1
            continue
        else :
            if max_count < count :
                max_count = count
            count = 0

    if max_count < count :
        max_count = count

    print (f'#{t} {max_count}')