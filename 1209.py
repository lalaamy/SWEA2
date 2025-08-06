for _ in range(1, 11) :
    
    tc = int(input())
    arr = [(list(map(int, input().split()))) for _ in range (100)]
    max_arr = 0


    # 행 순서로 총합
    max_n = 0
    for m in range(100):
        n_sum = 0
        for n in range(100) :
            n_sum += arr[m][n]
            
            if n_sum > max_n :
                max_n = n_sum
    

    # 열 순서로 총합
    max_m = 0
    for n in range(100):
        m_sum = 0
        for m in range(100):
            m_sum += arr[m][n]

            if m_sum > max_m:
                max_m = m_sum
    

    # n==m 대각선 총합
    mn_sum = 0
    max_mn = 0
    for n in range(100) :
        mn_sum += arr[n][n]

        if mn_sum > max_mn:
            max_mn = mn_sum

    
    # 역방향 대각선 총합
    rev_mn_sum = 0
    max_rev = 0
    
    for n in range (100) :
        rev_mn_sum += arr[n][99-n]

        if rev_mn_sum > max_rev :
            max_rev = rev_mn_sum


    max_list = [max_m, max_n, max_mn, max_rev]
    
    print (f'#{tc} {max(max_list)}')

