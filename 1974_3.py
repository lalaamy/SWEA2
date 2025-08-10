T = int(input())

for t in range(1, T+1) :
    arr = [(list(map(int,input().split()))) for _ in range(9)]

    success_count = 0

    for r in range(9) :
        r_idx = [0]*9
        for c in range(9) :
            r_idx[arr[r][c]-1] += 1
        
        if 0 not in r_idx :
            success_count += 1

    for c in range(9) :
        c_idx = [0]*9
        for r in range(9) :
            c_idx[arr[r][c]-1] += 1
        
        if 0 not in c_idx :
            success_count += 1
    
    for p in range(0, 9, 3) :
        for q in range(0, 9, 3) :

            square_idx = [0] * 9

            for m in range(3) :
                for n in range(3) :

                    square_idx[arr[p+m][q+n]-1] += 1
                
            if 0 not in square_idx :
                success_count += 1
    
    if success_count == 27 :
        print (f'#{t} 1')
    else :
        print (f'#{t} 0')