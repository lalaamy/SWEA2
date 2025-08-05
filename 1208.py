
# for i in range(1, 11) :

#     D = int(input())

#     T = list(map(int, input().split()))
#     for j in range(D) :
#         Max_num = max(T)
#         Min_num = min(T)

#         def dump_num (num, Max_num, Min_num) :
#             if Max_num-Min_num <= 1 or num == 0 :
#                 return Max_num - Min_num

#             else :
#                 max_after = Max_num -1
#                 min_after = Min_num +1
#                 return dump_num(num-1, max_after, min_after)
        
#     print(f'#{i}', dump_num(D, Max_num, Min_num))


# 필요 Data

# 덤프 수 : N
# 박스들의 높이 저장(길이 100) : boxes
# 덤프 마다의 최대값 : max_height
# 덤프 마다의 최소값 : min_height
# 덤프 마다의 최대값 인덱스 : max_idx
# 덤프 마다의 최소값 인덱스 : min_idx

# 구조
# 덤프 수 만큼 반복(N)
    # 덤프 작업이란?
    # ㄱ. 최대값, 최소값 구하고 해당 위치 저장(max_h, min_h)
    # ㄴ. 최대값에서 -1, 최소값에서 +1(boxes[max_idx], boxes[min_idx])
    # ㄷ. 단, 평탄화가 이뤄졌다면 덤프를 중단 > break
    #     평탄화란? > |최소-최대| <= 1


for i in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N) : # 덤프 작업을 N번 진행한다.
        boxes[boxes.index(max(boxes))] -= 1
        # min_box = min(boxes)
        boxes[boxes.index(min(boxes))] += 1
        # if max_box - min_box <= 1 : # 만일 최대와 최소 차이가 1 이하라면 바로 나가기
        #     break
        # max_box -= 1  # 아니면 최대에서 1 빼고
        # min_box += 1  # 아니면 최소에서 1 더하고

    print (f'#{i} {max(boxes) - min(boxes)}')

# max_idx = 0
# for j in range(1,len(boxes)):
#     if boxes[max_idx] <= boxes(j):
#         max_idx = i