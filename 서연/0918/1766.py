import sys
import heapq

N, M = map(int, sys.stdin.readline().split()) # 문제 수, 조건 수

inDegree =[0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

# print(inDegree)
# print(graph)

q = []

# 시작점 찾기
for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

# print(q)

result = []

while q:
    tmp = heapq.heappop(q)
    result.append(tmp)

    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

print(*result, sep=' ')