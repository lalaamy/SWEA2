for t in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))

    for n in range(N) :
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    print (f'#{t}', max(arr) - min(arr) )