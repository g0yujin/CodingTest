import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()

R, C, N = map(int, sys.stdin.readline().split())

map = [list(map(str, sys.stdin.readline().rstrip()))  for _ in range(R)]

def bfs(q,map): # map이 아니어도 정답이 되는 이유는?
    while q:
        x,y = q.popleft()
        map[x][y] = '.'
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx>=0 and nx<R and ny>=0 and ny<C and map[nx][ny] =='O':
                map[nx][ny] = '.'

def simulate(t):
    global q, map
    if t == 1:
        for i in range(R):
            for j in range(C):
                if map[i][j] == 'O':
                    q.append((i,j))
    elif t%2 == 1:
        # 3초가 지난 폭탄을 폭발시킨다.
        bfs(q,map)
        # 3초후에 터질 폭탄을 q에 다시 저장한다.
        for i in range(R):
            for j in range(C):
                if map[i][j] == 'O':
                    q.append((i,j))
    else:
        # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
        map = [['O']*C for _ in range(R)]

for i in range(1,N+1):
    simulate(i)

for i in map:
    print(''.join(i))