T = int(input())

for t in range (1, T+1) :
    N = int(input())
    arr = list(map(int, input()))

    count = 0
    result_count = 0
    for n in range(N) :
        if arr[n] == 1 :
            count += 1
            if arr[n+1] == 0 :
                if result_count < count :
                    result_count == count
                count = 0
            