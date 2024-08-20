import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
com = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    com[a].append(b)

comCnt = [0] *(n+1)

def check(n):
    que = deque()
    que.append(n)
    visited[n] = True
    while que:
        now = que.popleft()
        # 아래 자식 노드들로 가지를 뻗으므로 부모쪽을  + 1
        visited[now] = True
        comCnt[now] += 1
        for new in com[now]:
            if not visited[new]:
                que.append(new)

for i in range(n+1):
    check(i)
    visited = [False] * (n + 1)

tmpMax = max(comCnt)

for idx in range(n + 1):
    if comCnt[idx] == tmpMax:
        print(idx, end=" ")