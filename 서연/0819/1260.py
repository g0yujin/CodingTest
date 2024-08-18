import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M): # 총 M개의 간선
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = True
    graph[end][start] = True

DFS_visited = [False] * (N + 1)  # dfs의 방문기록
BFS_visited = [False] * (N + 1)  # bfs의 방문기록

def DFS(V): # DFS는 재귀로 구현  
    DFS_visited[V] = True
    print(V, end=' ')

    for i in range(1, N+1): # 1, 2, 3, ... , N
        if not DFS_visited[i] and graph[V][i]: # i를 방문하지 않았고, V랑 연결되어 있다면
            DFS(i)

def BFS(V): # BFS는 queue로 구현 -> deque
    q = deque([V])

    BFS_visited[V] = True
    while q: # q가 빌 때까지
        V = q.popleft() # 큐에 있는 첫 번째 값을 꺼냄
        print(V, end= ' ')
        for i in range(1, N+1):
            if not BFS_visited[i] and graph[V][i]:
                q.append(i)
                BFS_visited[i] = True

DFS(V)
print()
BFS(V)
