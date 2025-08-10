def bubble_sort(a, N) :
    a_copy = a[:]
    for i in range(N-1, 0, -1):
        for j in range(i) :
            if a_copy[j] > a_copy[j+1]:
                a_copy[j], a_copy[j+1] = a_copy[j+1], a_copy[j]
    return a_copy

T = int(input())

for t in range(T) : # 테스트 케이스 만큼 반복한다
    arr_len = int(input()) # 가로 길이를 입력한다.
    arr = list(map(int, input().split())) # 상자 리스트를 입력한다.
    arr_copy = bubble_sort(arr, len(arr)) # 오름차순 정렬을 만든다. 원본 arr은 그대로

    max_idx = 0
    for a in range(arr_len) : 
        for copy_a in range(len(arr_copy)) :
            if arr[a] == arr_copy[copy_a] : # 원래 있던 높이와 낙하 후 같은 높이의 상자가 있다면
                idx = copy_a - a # 그것을 낙차로 보고 차이를 구한다.
                if idx > max_idx : # 그게 가장 큰 것을 max로 치환한다.
                    max_idx = idx
                break
    print (f'#{t+1} {max_idx}')


# for t in range(1,T+1):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#     max_fall = 0
#     for i in range(N) :
#         fall = 0
#         for j in range(i+1, N):
#             if boxes[i] > boxes[j] :
#                 fall += 1
#         if fall > max_fall :
#             max_fall = fall
#     print (f'#{t} {max_fall}')


