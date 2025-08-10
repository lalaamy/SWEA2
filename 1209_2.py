for t in range(1, 11) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = []

    max_sum_r = 0
    for r in range (100) :
        sum_r = 0
        for c in range(100) :
            sum_r += arr[r][c]
        
            if max_sum_r <= sum_r :
                max_sum_r = sum_r
        
    sum_lst.append(max_sum_r)

    max_sum_c = 0
    for c in range (100) :
        sum_c = 0
        for r in range(100) :
            sum_c += arr[r][c]
        
            if max_sum_c <= sum_c :
                max_sum_c = sum_c

    sum_lst.append(max_sum_c)


    max_sum_i = 0
    sum_i = 0
    for i in range(100) :
        sum_i += arr[i][i]
    
        if max_sum_i <= sum_i :
            max_sum_i = sum_i
    
    sum_lst.append(max_sum_i)

    max_sum_j = 0
    sum_j = 0
    for j in range(100) :
        sum_j += arr[j][100-1-j]

        if max_sum_j <= sum_j :
            max_sum_j = sum_j

    sum_lst.append(max_sum_j)


    print (f'#{t}', max(sum_lst))