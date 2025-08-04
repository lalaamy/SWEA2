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
    for a in range(len(arr)) : 
        for copy_a in range(len(arr_copy)) :
            if arr[a] == arr_copy[copy_a] :
                idx = copy_a - a
                if idx > max_idx :
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


