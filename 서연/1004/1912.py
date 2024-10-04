# 시간 초과
# import sys

# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split())) # 0 ~ 9

# dp = [-1000] * n
 
# for i in range(n): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     for j in range(i+1):
#         dp[i] = max(dp[i], sum(arr[j:i+1]))
#         # print(dp)

# print(max(dp))

import sys

n = int(sys.stdin.readline()) # 10
arr = list(map(int, sys.stdin.readline().split())) # 0 ~ 9

for i in range(1, n): # 1, 2, 3, 4, 5, 6, 7, 8, 9
    arr[i] = max(arr[i], arr[i] + arr[i-1])

print(max(arr))