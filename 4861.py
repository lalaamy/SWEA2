T = int(input())


for t in range(1, T+1) :
    N, M = map(int, input().split())
    square = [(list(input())) for _ in range (N) ]
    new_square = [[0]*N for _ in range (N) ]

    for j in range(N):
        for i in range(N):
            new_square[j][i] = square[i][j]

    for r in range(N) :
        for c in range(N) :

            if len(square[r][c:c+M]) == M:
                temp = square[r][c:c+M]
                reverse = temp[::-1]

                if temp == reverse:
                    ans = temp
    
    for r in range(N) :
        for c in range(N) :

            if len(new_square[r][c:c+M]) == M:
                temp = new_square[r][c:c+M]
                reverse = temp[::-1]
                
                if temp == reverse:
                    ans = temp

    print (f'#{t} ',*ans, sep='')




        
    # for n in N :
    #     N_list = n
    #     N_rev = N_list[N-1, -1, -1]

    #     if N_list == N_rev :
    #         print (f'#{t} {N_list}')
    
    # 문장 통째로 뒤집기
    # for arr in square :
    #     N_list = []
    #     for n in arr :
    #         N_list.append(n)

    #     N_rev = N_list[::-1]

        # if N_list == N_rev :
        #     print (f'#{t} {N_list}')

    # 시작점 지정해서 뒤집기
    # for arr in square : # 전체 행렬에서 리스트 한줄씩 뽑기
    #     N_list = arr
    #     # for n in arr : # 리스트 한 줄에서 인자 하나 뽑기
    #     #     N_list.append(n) # 인자 하나씩 있는 리스트 완성
    #     N_part = []
    #     for i in range(M) : # 리스트 한 줄 길이만큼 반복문 돌기
    #             # for j in range(N-M+1) : # 리스트 내 시작점부터 M개만큼 꺼내기
    #         if i+M <= N :
    #             print(i, N_list[i])
    #             N_part.append(N_list[i])
    #     print(N_part)

    #     N_rev = N_part[::-1]
    
    #     print (N_rev)