N = int(input())
N_score = list(map(int, input().split()))
# N_result = []
for n in N_score :
    Bigger_list = [a for a in N_score if a > n]
    Smaller_list = [b for b in N_score if b < n]
    if len(Bigger_list) == len(Smaller_list) :
        print (n)
    else :
        continue
