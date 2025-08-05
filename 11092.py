T = int(input())

for t in range(1, T+1) : 
    N = int(input())
    ai = list(map(int, input().split()))
    max_idx = 0
    for i in range(1,len(ai)) :
        if ai[max_idx] <= ai[i]:
            max_idx = i
    min_idx = ai.index(min(ai))

    print (f'#{t} {abs(max_idx - min_idx)}')
