def bubble_sort(a) :
    a_copy = a[:]
    for n in range((len(arr)-1), 0, -1) :
        for i in range(n) :
            if a_copy[i] > a_copy[i+1] :
                a_copy[i], a_copy[i+1] = a_copy[i+1], a_copy[i]
    
    return a_copy


T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))
    arr_copy = bubble_sort(arr)

    max_fall = 0

    for n in range(N) :
        for i in range(N):
            if arr[n] == arr_copy[i] :
                fall = abs(i - n)
            
                if max_fall < fall :
                    max_fall = fall
                break
        
    print (f'#{t} {max_fall}')