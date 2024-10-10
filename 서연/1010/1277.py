import sys
import math
import heapq

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

n, w = map(int, sys.stdin.readline().split())
m = float(sys.stdin.readline())

dot = [[]]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    dot.append((a, b))

# print(dot) # [[], (0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 1), (4, 3)]

inf = 1e9
length = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): # 1 ~ 9
    for j in range(1, n+1): # 1 ~ 9       
        if i==j:  # 무시
            continue
        length[i][j] = dist(dot[i][0], dot[i][1], dot[j][0], dot[j][1])        
        if length[i][j] > m:
            length[i][j] = inf

for _ in range(w):
    a, b = map(int, sys.stdin.readline().split())
    length[a][b] = 0
    length[b][a] = 0

# for i in length:
#     print(*i)

result = [inf] * (n+1) # [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
result[1] = 0 # [inf, 0, inf, inf, inf, inf, inf, inf, inf, inf]

q = []
heapq.heappush(q, (0, 1)) # cost, start node

while q:
    cost, node = heapq.heappop(q) # 0, 1

    if result[node] < cost:
        continue

    for idx, i in enumerate(length[node]):
        if i == inf: # 길이가 m보다 크거나 본인일 때 무시
            continue

        newcost = cost + i
        if newcost < result[idx]:
            result[idx] = newcost
            heapq.heappush(q, (newcost, idx))

print(int(result[n]*1000))