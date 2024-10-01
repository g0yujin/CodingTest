# 방법 1
# import sys

# T = int(sys.stdin.readline())

# dp = [0] * 12

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4, 12):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# for _ in range(T):
#     n = int(sys.stdin.readline())

#     if n >= 4:
#         dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

#     print(dp[n])

# 방법 2
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])