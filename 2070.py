T = int(input())

for t in range (T) :
    N = list(map(int, input().split()))
    for n in range(len(N)-1):
        if N[n] > N[n+1] :
            print (f'#{t+1} >')
        elif N[n] == N[n+1] :
            print (f'#{t+1} =')
        else :
            print (f'#{t+1} <')