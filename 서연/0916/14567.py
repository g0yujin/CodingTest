import sys

N, M = map(int,sys.stdin.readline().split())

dp = [1] * (N+1)
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)

# print(arr)

for i in range(1, N+1): # 예제 1: 1, 2, 3

    for num in arr[i]:
        dp[num] = max(dp[num], dp[i] + 1)
    
print(*dp[1:])