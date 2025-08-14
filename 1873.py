T = int(input())
H, W = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, T+1) :
    for h in range(H) :
        game = list(input())

    N = int(input())
    arr = list(input())

    # for d in range(4) :

    #     nr = r + dr[d]
    #     nc = c + dc[d]

    for i in range(len(arr)) :
        if arr[i] == 'U':
            dir = [-1, 0]
            if arr[-1 + r, c] == "." :
                nr = r -1
                nc = c
            arr[r, c] = "."
            arr[nr, nc] = "^"
            r, c = nr, nc

        if arr[i] == 'D' :
            dir = [1, 0]
            if arr[1 + r, c] == "." :
                nr = r + 1
                nc = c
            arr[1 + r, c] = "v"
            r, c = nr, nc

        if arr[i] == 'L' : 
            dir = [0, -1]
            if arr[r, c - 1] == "." :
                nr = r 
                nc = c - 1
            arr[r, c - 1] = "<"
            r, c = nr, nc

        if arr[i] == 'R' :
            dir = [0, 1]
            if arr[r, c + 1] == "." :
                nr = r
                nc = c + 1
            arr[nr, nc] = '>'
            r, c = nr, nc

        if arr[i] == 'S':


    # for r in range(H) :
    #     for c in range(W) :
    #         if game[r][c] in ['^', 'v', '<', '>'] :
    #             start_point = game[r][c]
            
    #         if game[r][c] in [".", "*", "#", "-"] :
    
    