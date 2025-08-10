T = int(input())

for t in range(1, T+1) :
    N = int(input())
    cards = list(map(int, input()))

    arr_idx = [0]*10

    for i in cards :
        arr_idx[i] += 1

    max_card = 0
    max_count = 0
    
    for i in range(10):
        if max_count <= arr_idx[i] :
            max_count = arr_idx[i]
            max_card = i
    
    print(f'#{t} {max_card} {max_count}')