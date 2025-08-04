# for tc in range(1, 11):
#     N = int(input())
#     h = list(map(int, input().split()))
#     result = 0
#     for i in range(2, N - 1):
#         left = 0
#         right = 0
#         if h[i] > h[i - 1] and h[i] > h[i - 2]:
#             left += min(h[i] - h[i - 1], h[i] - h[i - 2])
#         if h[i] > h[i + 1] and h[i] > h[i + 2]:
#             right += min(h[i] - h[i + 1], h[i] - h[i + 2])
          
#         result += min(left, right)
#     print(f'#{tc} {result}')



# for tc in range(1,10+1):
#     T = int(input())
#     nums = list(map(int, input().split()))
#     ans = 0
#     for i in range(2, T-2):
#         if nums[i] == max(nums[i-2], nums[i-1], nums[i], nums[i+1], nums[i+2]):
#             view = nums[i] - max(nums[i-2], nums[i-1], nums[i+1], nums[i+2])
#             ans += view
#     print(f'#{tc} {ans}')


'''
# 데이터
- N : width
- heights : 건물들의 높이
- current_max : 길이 5 구간 내의 최대
- second_max : 길이 5 구간 내의 2번째 최대
- answer : 높이 누적합

# 로직
N < 입력

- 구간 돌아주기
  구간? : 중심점을 기준으로 -2 ~ +2 > 구간 중심점 : i
            for i in range(2, N-2)
            
            - 구간 내 current/second max를 구하기
               ㄱ. current max 구했더니 중심점과 크기가 같다면
                   > second max 구해서 current max와 차이를 answer에 누적
               ㄴ. 다르다면 > continue
'''

for t in range(1, 11) :
    N = int(input())
    b_lst = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2) :
        if max(b_lst[i-2], b_lst[i-1], b_lst[i], b_lst[i+1], b_lst[i+2]) == b_lst[i] :
            first_max = b_lst[i]
            second_max = max(b_lst[i-2], b_lst[i-1], b_lst[i+1], b_lst[i+2])
            result += first_max - second_max
    print (f'#{t} {result}')