# T = int(input())

# for t in range(1, T+1) :
#     N = int(input())
#     arr = [[0]*(N+1) for _ in range(N+1)]
#     arr[0][0] = 1
#     print(f'#{t}')
#     for i in range(1, N+1) :
#         for j in range(1, i+1) :
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#             print(arr[i][j], end=' ')
#         print()

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]* (N+1) for _ in range(N+1)]
    arr[0][0] = 1
    print (f'#{t}')
    for n in range(1, N+1):
        for i in range(1, n+1):
            arr[n][i] = arr[n-1][i-1] + arr[n-1][i]
            print (arr[n][i], end = ' ')
        print ()