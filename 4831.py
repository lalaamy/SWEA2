# k, n, m = map(int, input().split())
# init_k = k

# charge = 0
# stop = list(map(int, input().split()))


# for i in range (1, n+1) :
#     k -= 1

#     if k < 0 :
#         charge = 0
#         break

#     if i not in stop :
#         continue
    
#     # 남은 연료로 종점을 가지 못할 때
#     # and 다음 충전소도 못 갈 때
#         # 여기가 마지막 충전소일 때
#         # or 다음 충전소 까지 갈 연료 안 될 때
#     # 작성 순서 중요 / 바뀌면 안 됨
#     if i+k < n and (stop.index(i) == len(stop)-1 or i+k < stop[stop.idex(i)+1]):
#         k = init_k
#         charge += 1



T = int(input())

for t in range(1, T+1) :

    k, n, m = map(int, input().split())
    stop = list(map(int, input().split()))

    i = 0 # 현재 위치 
    charge = 0 # 충전 횟수 (추후 프린트될 수)

    while (i+k) < n : # 현재 위치에서 충전 후 갈 수 있는 칸 수까지 한 게 전체 길이 내에 있을 때만 진행한다.
        for j in range(i+k, i, -1) :
            if j in stop :
                i = j
                charge += 1
                break
        else :
            charge = 0
            break
    
    print (f'#{t} {charge}')