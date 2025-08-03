I = int(input())

# lst = []

for i in range(1, I+1) :
    if I % i != 0 :
        continue
    else :
        print (i, end =' ')