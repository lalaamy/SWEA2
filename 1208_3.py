for t in range(1, 11) :
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N) :
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
    
    print (f'#{t}', max(boxes)- min(boxes))