numbers = [1,2,3,4,5]
M = 3

picked_num = []
visited = [0]*len(numbers)


def perm (count) :
    if count == M :
        return
    for i in range(len(numbers)):
        if visited == 1 :
            continue
        picked_num.append(numbers[i])
        visited[i] = 1
        perm(count+1)
        picked_num.pop()
        visited[i] = 0

perm(0)