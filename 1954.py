T = int(input())

for t in range(1, T+1) :

    result = 1

    for n in range(3) :
        for i in range(N) :
            for di, dj in [[-1,0], [1,0], [0,-1], [0,1]] :
                if n % 2 == 0 :
                    arr[0*di][i*dj] = result
                    