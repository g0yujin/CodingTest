import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dp =[0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M): # 학생들 간의 키 순서 정보, 앞에 있는 학생 수 정리
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    dp[b] += 1

# print(dp) # 예제 2: [0, 1, 1, 0, 0]
# print(graph) # 예제 2: [[], [], [], [1], [2]]

q = deque()

# 시작점 찾기
for i in range(1, N+1): # 1, 2, 3, 4
    if dp[i] == 0:
        q.append(i)

# print(q)

result = []

while q:
    tmp = q.popleft()
    result.append(tmp)

    for i in graph[tmp]:
        dp[i] -= 1
        if dp[i] == 0:
            q.append(i)

print(*result, sep=' ')