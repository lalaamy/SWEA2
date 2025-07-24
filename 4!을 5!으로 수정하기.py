n = 5 # 변경 X > 목적지이기 때문
answer = 1

def fact(depth):
    global answer
    if n == depth:
        return
    else:
        depth += 1
        answer *= depth
        fact(depth)
        
fact(1)
print(answer)