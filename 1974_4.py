T = int(input())

for t in range(1, T+1) :

    arr = [list(map(int, input().split())) for _ in range(9)]

    c_count = 0
    for r in range(9) :
        count_idx = [0]*10
        count_idx[0] = 1
        for c in range(9) :
            count_idx[arr[r][c]] += 1
        if 0 in count_idx :
            result = 0
            break
        else :
            c_count += 1
    
    r_count = 0
    for c in range(9) :
        count_idx = [0]*10
        count_idx[0] = 1
        for r in range(9) :
            count_idx[arr[r][c]] += 1
        if 0 in count_idx :
            result = 0
            break
        else :
            r_count += 1
    
    square_count = 0
    for r in range(0, 9, 3) :
        for c in range(0, 9, 3) :
            count_idx = [0] * 10
            count_idx[0] = 1
            for i in range(3) :
                for j in range(3) :
                    count_idx[arr[i][j]] += 1
            if 0 in count_idx :
                result = 0
                break
            else :
                square_count += 1   
    
    if r_count + c_count + square_count == 27 :
        result = 1
    print (f'#{t} {result}')