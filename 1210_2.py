
dr = [-1, 0, 0]
dc = [0, -1, 1]

search_d = [[1,2,0], [0,1], [0,2]]

for t in range(1, 11) :
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = ladder[99].index(2)

    d = 0

    while r > 0 :
        for i in range(len(search_d[d])):
            next_d = search_d[d][i]
            next_r = r + dr[next_d]
            next_c = c + dc[next_d]

            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1 :
                d, r, c = next_d, next_r, next_c
                break

    print (f'{t} {c}')