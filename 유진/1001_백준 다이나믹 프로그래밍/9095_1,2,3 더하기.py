import sys

T = int(sys.stdin.readline())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for j in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])




# dp[1] = 1
# dp[2] = 11, 2 = 2
# dp[3] = 111,12,21,3 = 4
# dp[4] = 1111, 112, 121, 211, 31, 13, 22 = 7
# dp[5] = 11111, 1112, 1121, 1211, 2111, 311, 131, 113, 122, 212, 221, 32, 23 = 13
# dp[6]

# dp[4] = dp[1] + dp[2] + dp[3]
# dp[5] = dp[2] + dp[3] + dp[4]
