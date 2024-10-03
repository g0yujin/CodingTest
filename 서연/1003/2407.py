import sys

n, m = map(int, sys.stdin.readline().split())

dp = [ [0 for j in range(n+1)] for i in range(n+1) ]

# print(dp)

for i in range(1, n+1):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(2, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])


# # factorial 사용
# # import math
# # math.factorial(n)
# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# n, m = map(int, input().split())

# print(fact(n)//(fact(n-m)*fact(m)))



# # 라이브러리 사용
# from math import comb
# n, m = map(int, input().split())
# print(comb(n, m))