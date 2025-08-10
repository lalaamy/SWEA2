
arr = [list(map(int, input().split())) for _ in range(5)]

# max_sum = 0

# sum_i = 0
# for i in range(5) :
#     sum_i += arr[i][i]

# if max_sum <= sum_i :
#     max_sum = sum_i

#     sum_i = 0

# print (max_sum)

max_sum = 0
sum_j = 0
for j in range(5) :
    sum_j += arr[j][5-1-j]

if max_sum <= sum_j :
    max_sum = sum_j

    sum_j = 0

print (max_sum)