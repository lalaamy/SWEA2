
for i in range(10) :
    print(f'#{i+1}')

D = int(input())

100 * 100 정렬

def dump_num (num, max, min) :
    if max-min <= 1 or num == 0 :
        return max-min

    else :
        max_after = max-1
        min_after = min+1
        return dump_num(num-1, max_after, min_after)
    
print(f'#{i+1}', dump_num(D, max_list, min_list))


