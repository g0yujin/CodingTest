# # 방법 1
# import sys

# N = int(sys.stdin.readline())
# tmp = N

# if N % 4 == 1 or N % 4 == 3:
#     print('SK')
# elif N % 4 == 0 or N % 4 == 2:
#     print('CY')

# 방법 2
import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]

for i in range (1, N+1):
    dp[i] = int(i/3) + int(i%3) 
    print(i, dp[i])

print('SK' if dp[N] % 2 == 1 else 'CY')

# # 방법 3
# import sys

# N = int(sys.stdin.readline())

# if N % 2 == 0:
#     print('CY')
# else:
#     print('SK')