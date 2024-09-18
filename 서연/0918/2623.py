import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # N: 가수의 수, M: PD의 수
graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for _ in range(M):
    a, *b = map(int, sys.stdin.readline().split())
    
    for i in range(a-1):
        graph[b[i]].append(b[i+1])
        inDegree[b[i+1]] += 1

    # print(graph)
    # print(inDegree)

q = deque()

# 시작점 찾기
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

result = []

while q:
    tmp = q.popleft()
    result.append(tmp)

    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)

if len(result) == N:
    print(*result, sep='\n')
else:
    print(0)