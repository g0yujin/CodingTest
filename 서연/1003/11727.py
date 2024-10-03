# 방법 1
# import sys

# n = int(sys.stdin.readline())

# dp = [0] * (n+1)

# for i in range(1, n+1):
#     if i == 1:
#         dp[i] = 1
#     else:
#         if i % 2 == 0:
#             dp[i] = dp[i-1]*2 + 1
#         else:
#             dp[i] = dp[i-1]*2 - 1

# print(dp[n]%10007)

# # 방법 2
# import sys

# n = int(sys.stdin.readline())
# dp = [0] * (n+1)

# dp[1] = 1

# if n >= 2:
#     dp[2] = 3
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + 2 * dp[i-2]

# print(dp[n]%10007)

# 방법 3
a=b=1
for i in range(int(input())):
	a,b=b,2*a+b
     
print(a%10007)