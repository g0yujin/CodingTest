import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split()) # 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X

arr = [ [] for _ in range(N+1) ]
length = [987654321]*(N+1)
visited = [0] *(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    arr[a].append(b)
    # arr[b].append(a)

def bfs(x):
    q = deque([x]) # 1
    visited[x] = 1
    length[x] = 0

    while q:
        v = q.popleft() # 1

        visited[v] = 1 # 방문 처리

        for i in arr[v]: # 2, 3
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)

                length[i] = min(length[i], length[v]+1)

    return None

bfs(X)

# print(length)

if length.count(K) == 0:
    print(-1)
else:
    for idx, i in enumerate(length):
        if i == K:
            print(idx)