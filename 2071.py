T = int(input())

for t in range(T) :
    N = list(map(int, input().split()))
    
    print(f'#{t+1} {round(sum(N)/len(N))}')