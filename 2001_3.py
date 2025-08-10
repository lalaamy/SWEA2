T = int(input())

for t in range(1, T+1) :
    n, m = map(int, input().split())
    arr =[(list(map(int, input().split()))) for _ in range(n)]

    sum_list = []

    for r in range(n-m+1) :
        for c in range(n-m+1) :
            m_sum = 0

            for i in range(m) :
                for j in range(m) :
                    m_sum += arr[r+i][c+j]
            
            sum_list.append(m_sum)


    print (f'#{t}', max(sum_list))