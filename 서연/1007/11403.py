# import sys
# from collections import deque

# N = int(sys.stdin.readline().strip())

# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# result = [[0] * (N) for _ in range(N)]

# def bfs(x):
#     q = deque([x])
    
#     visited= [0 for _ in range(N)]

#     while q:
#         v = q.popleft()

#         for i in range(N):
#             if visited[i] == 0 and arr[v][i] == 1:
#                 q.append(i)
#                 visited[i] = 1
#                 result[x][i] = 1

# for i in range(N):
#     bfs(i)

# for j in result:
#     print(*j)


import sys
from collections import deque

N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):

            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in arr:
    print(*i)