
for i in range(1, 11) :

    D = int(input())

    T = list(map(int, input().split()))
    Max_num = max(T)
    Min_num = min(T)

    def dump_num (num, Max_num, Min_num) :
        if Max_num-Min_num <= 1 or num == 0 :
            return Max_num - Min_num

        else :
            max_after = Max_num -1
            min_after = Min_num +1
            return dump_num(num-1, max_after, min_after)
        
    print(f'#{i}', dump_num(D, Max_num, Min_num))


