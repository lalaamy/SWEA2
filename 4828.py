T = int(input())

for t in range(1, T+1) :
    N = int(input())
    a_lst = list(map(int, input().split()))
    max_int = 0
    min_int = 1000000
    for n in a_lst:
        if max_int < n :
            max_int = n
        if min_int > n :
            min_int = n
    print (f'#{t} {max_int - min_int}')





T = int(input())

for t in range(1, T+1) :
    N = int(input())
    N_arr = list(map(int, input().split()))
    print (max(N_arr) - min(N_arr))