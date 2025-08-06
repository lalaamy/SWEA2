T = int(input())

for t in range(1, T+1) :
    arr = [list(map(int, input().split())) for _ in range (9)]

    result = 0

    for n in range(9) :
        m_arr = [0] * 9
        for m in range (9) :
            m_arr[arr[n][m]-1] += 1

        if 0 not in m_arr :
            result += 1


    
    for m in range(9) :
        n_arr = [0] * 9
        for n in range (9) :
            n_arr[arr[n][m]-1] += 1

        if 0 not in n_arr :
            result += 1

    
    for p in range (0, 9 ,3):
        for q in range (0, 9, 3):
            pq_arr = [0] * 9
            for i in range(3) :
                for j in range(3) :
                    pq_arr[arr[p+i][q+j]-1] += 1
            
            if 0 not in pq_arr :
                result += 1


    if result != 27 :
        result_total = 0
    else :
        result_total = 1
    

    print (f'#{t} {result_total}')