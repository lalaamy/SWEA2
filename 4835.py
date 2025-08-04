T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    v = list(map(int, input().split()))
    max_sum = sum(v[0:M])
    min_sum = sum(v[0:M])
    for i in range(N-M+1) :
        v_sum = sum(v[i:i+M])
        if v_sum > max_sum :
            max_sum = v_sum
        if v_sum < min_sum :
            min_sum = v_sum
    print (f'#{t} {max_sum - min_sum}')