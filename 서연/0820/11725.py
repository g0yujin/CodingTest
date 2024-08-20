import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(n+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()

res = ans[2:]
for x in res:
    print(x)

# print('\n'.join(map(str, ans[2:])))
    