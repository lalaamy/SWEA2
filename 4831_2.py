T = int(input())

for t in range(1, T+1) :
    K, N, M = map(int, input().split())
    stop = list(map(int, input().split()))

    i = 0 # 현재 위치
    charge_count = 0 # 충전한 횟수

    while (i+K) < N :
        for j in range(i+K, i, -1):
            if j in stop :
                i = j
                charge_count += 1
                break

        else :
            charge_count = 0
            break

    print (f'#{t} {charge_count}')