import sys

R, C = map(int, sys.stdin.readline().split())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

# 늑내가 양이 있는 칸으로 갈 수 있으면 True, 아니라면 False
check = False

# 좌/우/위/아래 방향 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for r in range(R):
    for c in range(C):
        if graph[r][c] == 'W':
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if graph[nr][nc] == 'S':
                        check = True
                        break


if check:
    print(0)
else:
    print(1)
    # 늑대와 양이 있는 위치를 제외하고 모두 울타리 설치
    for r in range(R):
        for c in range(C):
            if graph[r][c] == '.':
                graph[r][c] = 'D'

    for i in graph:
        print(''.join(i))