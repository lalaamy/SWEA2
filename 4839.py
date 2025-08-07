
def binarySearch(end, key) :
    start = 1

    count = 0

    while start <= end :
        middle = int((start+end)/2)
        if middle == key :
            count += 1
            return count
        
        elif middle < key :
            start = middle
            count += 1
        else :
            end = middle
            count += 1
    
    return count



T = int(input())

for t in range(1, T+1) :
    P, Pa, Pb = map(int, input().split())

    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)

    if  A < B :
        print (f"#{t} A")
    
    elif A > B :
        print (f"#{t} B")
    
    else :
        print (f"#{t} 0")