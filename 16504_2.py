def Bubble_sort(a) :
    copy_a = a[:]
    for i in range(len(a)-1, 0, -1) :
        for j in range(i) :
            if copy_a[j] > copy_a[j+1] :
                copy_a[j], copy_a[j+1] = copy_a[j+1], copy_a[j]
    return copy_a

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    boxes = list(map(int, input().split()))
    boxes_copy = Bubble_sort(boxes)

    max_fall = 0
    for i in range(len(boxes)) :
        for j in range(len(boxes_copy)) :
            if boxes[i] == boxes_copy[j] :
                fall = j - i
                if max_fall < fall :
                    max_fall = fall
                break
    
    print (f'#{t} {max_fall}')