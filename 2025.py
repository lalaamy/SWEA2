def sum_T(P) :
        if P == 1 :
            return 1
        else :
            return P + sum_T(P-1)
        
T = int(input())
print (sum_T(T))