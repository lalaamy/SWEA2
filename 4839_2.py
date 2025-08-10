def binarySearch(n, key) :
    start = 1

    count = 0

    while start <= n :
        middle = int((start+n)/2)

        if middle > key :
            n = middle
            count += 1
        
        elif middle < key :
            start = middle 
            count += 1

        else :
            count += 1
            return count
    
    return count

T = int(input())

for t in range(1, T+1) :
    p, pa, pb = map(int, input().split())

    count_a = binarySearch(p, pa)
    count_b = binarySearch(p, pb)

    result = ''
    if count_a < count_b :
        result += 'A'
    elif count_a > count_b :
        result += 'B'
    else :
        result += '0'
    
    print (f'#{t} {result}')