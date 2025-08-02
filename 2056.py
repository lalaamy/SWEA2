T = int(input())

for t in range(T) :
    YMD = input()
    Year = int(YMD[:4])
    Month = int(YMD[4:6])
    Day = int(YMD[6:])
    if Month == 2:
        if 28 >= Day >= 1 :
            print (f'#{t+1} {Year:04d}/{Month:02d}/{Day:02d}')
        else :
            print (f'#{t+1} -1')
    elif Month in [4, 6, 9, 11] :
        if 30 >= Day >= 1 :
            print (f'#{t+1} {Year:04d}/{Month:02d}/{Day:02d}')
        else :
            print (f'#{t+1} -1')
    elif Month in [1, 3, 5, 7, 8, 10, 12] :
        if 31 >= Day >= 1 :
            print (f'#{t+1} {Year:04d}/{Month:02d}/{Day:02d}')
        else :
            print (f'#{t+1} -1')
    else :
        print (f'#{t+1} -1')

