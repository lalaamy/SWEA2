# stack = [0] * 10000
# top = -1

for t in range (1, 11) :
    N = int(input())

    infix = input()

    for token in infix :
        #피연산자일 때 후위식에 추가하는 것
        if token != '+' :
            postfix += token
        # 연산자일 때
        else :
            top==-1 # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = token

# for t in range (1, 11) :
#     N = int(input())

#     infix = input()

    stack = ''
    top = -1

    for x in infix:
        if x !='+': # 피연산자면...
            top += 1            # push(x)
            stack[top] = int(x)
        else:
            a= stack[top]
            top -= 1  # pop()
            b = stack[top]
            top -= 1  # pop()            
            # op1 + op2
            top += 1    # push()
            stack[top] = a + b

    print (f'#{t} {stack[top]}')