# 정렬
T = int(input())

for t in range (1, T+1) :

    N, K = map(int, input().split()) 
    stats = list(map(int, input().split()))

    answer = 1 # 1명이면 팀의 개념이 아니기 때문에

    stats.sort() # 원본을 바꿔도 되니까


    for i in range(N-1) : # 끝 점을 넣으면 팀이 1명인 것까지 고려하게 되는 거니까
        temp = 1 # 팀원 누적할 것임. 이건 팀 초깃값
        for j in range (i+1, N) :
            if stats[j] - stats[i] > K : # 멈출 조건
                break
            else :
                temp += 1
        
        answer = max(answer, temp)

    print(f'#{t} {answer}')


# 투 포인터

T = int(input())

for t in range (1, T+1) :

    N, K = map(int, input().split()) 
    stats = list(map(int, input().split()))

    answer = 1 # 1명이면 팀의 개념이 아니기 때문에

    stats.sort() # 원본을 바꿔도 되니까

    left = 0
    right = 0

    while right < N :

        if stats[right] - stats[left] <= K :
            right += 1
            answer = max(answer, right - left)
            continue
        left += 1 # right 못 갈 때

    print (answer)