T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [(list(map(int, input().split()))) for _ in range (N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range (N) :
        for c in range (N) :
            r_sum = arr[0:N-1][c]
            c_sum = arr[r][0:N-1]
    
print (c_sum)