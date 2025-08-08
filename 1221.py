
T = int(input())

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for t in range(1, T+1) :
    input()
    str_num_lst = list(input().split())

    result = []
    for num in numbers :  # number 이라는 리스트에서 하나씩 꺼낸다.
        for str in str_num_lst : # input 받은 리스트에서 인자 하나씩 꺼낸다.
            if num == str : # 만일 그 두개의 문자가 동일하다면
                result.append(str) # 차례대로 리스트에 넣는다.

    print (f'#{t}')
    print (' '.join(result))