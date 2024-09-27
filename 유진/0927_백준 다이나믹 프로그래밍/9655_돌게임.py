import sys

N = int(sys.stdin.readline())

# 리스트 초기화
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = int(i / 3) + int(i % 3)
    print(i, dp[i])

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')