# T = int(input())
# numbers = list(input())
# arr = [0] * 101

# for i in range (101) :
#     arr[i] += 1
#     arr.count()

# N = int(input())


# 강사님 풀이
T = int(input())

for _ in range(1, T+1) :
    tc = int(input())
    answer = 0

    scores = list(map(int, input().split()))
    score.sort(reverse=True)

# 현재 카운팅 > current_count
# 누적 카운팅 최대 > max_count
# 이전 값 > before_score
    current_count = 0 # 무슨 수여도 상관 없음
    max_count = 0 # 어떤 수와 비교해도 작아야 함
    before_score = -1 # 초기값이 0일 때 비교도 하려고

    for score in scores :
        if before_score != score :
            if max_count < current_count :
                max_count = current_count
                answer = before_score
            current_count = 1
        else :
            current_count += 1
        before_score = score

    print(f'#{tc} {answer}')