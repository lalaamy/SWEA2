T = int(input())

for t in range(1, T+1) :
    txt = input()

    top = -1
    stack = [0] * (len(txt))

    ans = 1

    for x in txt :
        if x in ['(', '{'] :
            top += 1 # 탑 수 늘려주고
            stack[top] = x # 그 탑에 그 괄호 넣어주기
        if x in [')', '}'] :
            if top == -1 :
                ans = 0
                break
            elif x == ")" :
                if stack[top] != '(' :
                    ans = 0   
                    break     
            elif x == '}' :
                if stack[top] != '{' :
                    ans = 0
                    break
            top -= 1

    if top != -1 :
        ans = 0

    print (f'#{t} {ans}')