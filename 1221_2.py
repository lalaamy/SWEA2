T = int(input())

for t in range(1, T+1) :
    input()
    arr = list(map(str, input().split()))
    num_eng = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    ans = []

    for i in num_eng :
        for j in arr :
            if i == j :
                ans.append(j)

    print (f'#{t}')
    print (' '.join(ans))