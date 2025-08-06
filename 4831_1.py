T = int(input())

for t in range(1, T+1):
    k, n, m = map(int, input().split())

    fuel = k
    position = 0
    answer = 0
    recent_stop_idx = 0

    while position + fuel < n : # fuel은 무조건 K (충전소 갈 때마다 풀충)
        # 충전소로만 이동할 거니까 충전소 번호만 보면 됨
        # 현재 위치 + 연료 ; 최대일 때의 충전소로 간다.

        next_stop_idx  = recent_stop_idx

        # 다음 충전소 탐색
        for idx in range (recent_stop_idx +1, M):
            if charges[idx] > position + fuel :
                break
            
            next_stop_idx = idx

        if next_stop_idx == recent_stop_idx :
            answer = 0
            break
        
        # 다음 충전소를 찾았을 때
        position = charges[next_stop_idx]
        answer += 1
        recent_stop_idx = next_stop_idx
