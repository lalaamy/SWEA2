T = int(input())

for tc in range(1, T+1) :
    answer = 0  # 누적합을 구할 거라 처음은 0으로 시작
    N = int(input())
    crops = [list(map(int, input())) for _ in range(N)] # 2차배열

    for r in range(N) : # 행
        col_idx = abs((N//2) - r) # 시작인덱스

        col_count = N - ((abs(N//2)-r)*2) # 반복 횟수

        for c in range(col_idx, col_idx + col_count) : # 열
            answer += crops[r][c]


    print(f'#{tc} {answer}')