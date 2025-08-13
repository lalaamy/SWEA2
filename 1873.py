T = int(input())
H, W = map(int, input().split())

for t in range(1, T+1) :
    for h in range(H) :
        game = list(input())

    N = int(input())
    arr = list(input())

    for r in range(H) :
        for c in range(W) :
            if game[r][c] in ['^', 'v', '<', '>'] :
                start_point = game[r][c]