T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M) :
        i, j = map(int, input().split())

        idx = i - 1

        for cnt in range(1, j+1) :
            if 0 <= idx+cnt < N and 0 <= idx-cnt < N :
                if arr[idx-cnt] == arr[idx+cnt] :
                    arr[idx-cnt] = 1 - arr[idx-cnt]
                    arr[idx+cnt] = 1 - arr[idx+cnt]
    
    print (f'#{t}',*arr)
