T = int(input())

for t in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for r in range(n):
        count = 0
        for c in range(n):

            if arr[r][c] == 1:
                count += 1
                continue
            else :
                if count == m :
                    result += 1
                count = 0

        if count == m :
            result += 1
    

    for c in range(n):
        count = 0
        for r in range(n):

            if arr[r][c] == 1:
                count += 1
                continue
            else :
                if count == m :
                    result += 1
                count = 0

        if count == m :
            result += 1
    
    print (f'#{t} {result}')