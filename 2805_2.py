T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    crop_sum = 0

    for r in range(N) :
        start_idx = abs(N//2-r)
        count_idx = N - (abs(N//2-r) * 2)
        for c in range(start_idx, start_idx+count_idx) :
            crop_sum += arr[r][c]

    print (f'#{t} {crop_sum}')