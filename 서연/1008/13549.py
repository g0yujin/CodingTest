import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque([n])

visited = [-1 for _ in range(100001)]

visited[n] = 0

while q:
    v = q.popleft()

    if v == k: # 도착
        print(visited[v])
        break

    for nx in (v-1, v*2, v+1):
        if nx == v*2:
            if 0 <= nx < 100001 and visited[nx] == -1:
                visited[nx] = visited[v]
                q.appendleft(nx)
        else:
            if 0 <= nx < 100001 and visited[nx] == -1:
                visited[nx] = visited[v]+1
                q.append(nx)

    # if 0 <= v-1 < 100001 and visited[v-1] == -1:
    #     visited[v-1] = visited[v]+1
    #     q.append(v-1)
    # if 0 <= v*2 < 100001 and visited[v*2] == -1:
    #     visited[v*2] = visited[v]
    #     q.appendleft(v*2)
    # if 0 <= v+1 < 100001 and visited[v+1] == -1:
    #     visited[v+1] = visited[v]+1
    #     q.append(v+1)