# # 방법 1
# import sys

# N = int(sys.stdin.readline())

# num = [0] + list(map(int, sys.stdin.readline().split()))

# def solution(start, end):
#     result = 0
#     while start <= end:
#         mid = (start + end) // 2

#         visited = [False] * (N+1)
#         flag = False

#         # 첫 번째 돌부터 탐색 시작
#         stack = [1]
#         visited[1] = True

#         while stack:
#             now = stack.pop()

#             if now == N:
#                 flag = True
#                 break

#             for idx in range(now+1, N+1):
#                 temp = (idx - now) * (1 + abs(num[now] - num[idx]))

#                 if temp <= mid and not visited[idx]:
#                     stack.append(idx)
#                     visited[idx] = True

#         if flag:
#             result = mid
#             end = mid - 1
#         else:
#             start = mid + 1
    
#     return result

# print(solution(1, (N-1) * (1 + abs(num[N] - num[1]))))

# 방법 2
INF = 999999999
n = int(input())
A = list(map(int, input().split()))
# dp[i]는 i까지 가는데 드는 최소 힘
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j]) 
        dp[i] = min(dp[i], power)

print(dp[-1])