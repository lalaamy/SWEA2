T = int(input())

for t in range(T) :
    Test = 0
    N = list(map(int,input().split()))
    for i in range(10):
        if N[i] % 2 == 1 :
            Test += N[i]
    print (f'#{t+1} {Test}')