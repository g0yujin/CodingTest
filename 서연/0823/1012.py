import sys

T = int(sys.stdin.readline())

def BFS(x, y):
    stack = [(x, y)]
    graph[x][y] = 0 # 방문한 곳은 0으로 바꿔줌

    while stack:
        x, y = stack.pop()
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                stack.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    cnt = 0

    for m in range(M):
        for n in range(N):
            if graph[m][n] == 1:
                BFS(m, n)
                cnt += 1
    print(cnt)