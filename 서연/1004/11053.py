import sys

A = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * A
 
for i in range(1, A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))