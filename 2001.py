T = int(input())

for tc in range(1, T+1) :
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for n1 in range(N-M+1) : # 행에서 파리채 시작점이 되어도 되는 구간
        for n2 in range(N-M+1) : # 열에서 파리채 시작점이 되어도 되는 구간
            total = 0
            for m1 in range(M) :
                for m2 in range(M) :
                    total += arr[n1+m1][n2+m2]
            
            if total >= result :
                result = total
    print (f'#{tc} {result}')