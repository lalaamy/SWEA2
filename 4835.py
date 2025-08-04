T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for n in range(N-2) :
        # max_sum = 0
        # min_sum = 0
        for m in range(M):
            max_sum = int(max(sum(lst[m:m+3])))
            min_sum = int(min(sum(lst[m:m+3])))
    print (f'#{t} {max_sum - min_sum}')