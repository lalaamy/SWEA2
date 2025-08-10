T = int(input())

for t in range(1, T+1) :
    arr = [(list(map(int, input().split()))) for _ in range(9)]
    result = 0


    for r in range (9) :
        idx = ([0]*9)
        for c in range (9) :
            idx[arr[r][c]-1] += 1
        if 0 not in idx :
            result += 1
    
    for c in range (9) :
        idx = ([0]*9)
        for r in range (9) :
            idx[arr[r][c]-1] += 1
        if 0 not in idx :
            result += 1


    for r in range(0, 9, 3) :
        for c in range(0, 9, 3) :
            idx = ([0]*9)
            for i in range(3):
                for j in range(3) :
                    idx[arr[r+i][c+j]-1] += 1

            if 0 not in idx :
                result += 1


    if result == 27 :
        print (f'#{t} 1')
    else :
        print (f'#{t} 0')