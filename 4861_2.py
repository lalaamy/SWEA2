T = int(input())

for t in range(1, T+1) :
    n, m = map(int, input().split())

    arr = [list(map(str, input())) for _ in range(n)]
    new_arr = [[0]*n for _ in range(n)]

    for c in range(n):
        for r in range(n) :
            new_arr[r][c] = arr[c][r]

    for r in range(n) :
        for c in range(n) :
            if len(arr[r][c:c+m]) == m:
                temp = arr[r][c:c+m]
                reverse = temp[::-1]
                if temp == reverse :
                    ans = temp

    for r in range(n) :
        for c in range(n) :
            if len(new_arr[r][c:c+m]) == m:
                temp = new_arr[r][c:c+m]
                reverse = temp[::-1]
                if temp == reverse :
                    ans = temp
    
    print (f'#{t} ', *ans, sep='')
