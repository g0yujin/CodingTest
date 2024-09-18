import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    temp = list(map(int, input().split()))
    for i in range(len(temp)-2):
        graph[temp[i+1]].append(temp[i+2])
        indegree[temp[i+2]] += 1

result = []
q = deque()

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != v:
    print(0)
else:
    for i in result:
        print(i)
