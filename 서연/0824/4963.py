import sys
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y):
    field[x][y] = 0
    q = deque()
    q.append([x, y])
    
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append([nx, ny])

while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    count = 0
    field = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)