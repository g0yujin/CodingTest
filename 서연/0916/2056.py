import sys

N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(1, N+1):
    time, cnt, *nums = map(int, sys.stdin.readline().split())
    dp[i] = time

    for num in nums:
        dp[i] = max(dp[i], dp[num] + time)
    
    # print(dp)

print(max(dp))

