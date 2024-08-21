import sys

N = int(sys.stdin.readline())

graph = []
num = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1: #만약 집이 있으면
        global count
        count += 1 #집의 수 1개 추가
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

count = 0
result = 0

for i in range(N):
    for j in range(N):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort() # 오름차순 정렬
print(result) # 몇단지까지 있는지

for i in range(len(num)):
    print(num[i])