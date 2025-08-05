T = int(input())

for t in range(1, T+1) :
    N = int(input())
    ai = list(map(int,input()))

    count = [0] * 10
    max_count = 0
    max_a = 0

    for i in ai : # 예를 들어 7797946543
        count[i] += 1
    for i in range(10):
        if max_count <= count[i] :
            max_count = count[i]
            max_a = i

    print (f'#{t} {max_a} {max_count}')