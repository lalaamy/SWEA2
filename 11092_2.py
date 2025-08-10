T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))
    # c_arr = arr[:]
    # set_arr = set(c_arr)

    # min_arr = min(arr)
    # max_arr = max(arr)

    min_idx = len(arr)
    max_idx = -1

    for i in range(len(arr)) :
        if arr[i] == min(arr) :
            if i < min_idx :
                min_idx = i
            # min_idx = i
        # break

    for j in range(len(arr)-1, -1, -1) :
        if arr[j] == max(arr) :
            if j > max_idx :
                max_idx = j
            # max_idx = j
        # break

    result = abs(max_idx - min_idx)

    print(f'#{t} {result}')
