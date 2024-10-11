# # 방법 1
# import sys
# import heapq

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# arr = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, sys.stdin.readline().split())
    
#     arr[a].append((b, c))

# # print(arr) # [[], [(2, 2), (3, 3), (4, 1), (5, 10), (4, 2)], [(4, 2)], [(4, 1), (5, 1), (5, 10), (1, 8), (4, 2)], [(5, 3)], [(1, 7), (2, 4)]]

# inf = 1e9

# def sol(start):

#     distance = [inf] * (n+1) # [inf, 0, inf, inf, inf, inf]

#     q=[]
#     heapq.heappush(q, (0, start))
#     distance[start] = 0 

#     while q: # (0, 1)
        
#         dist, now = heapq.heappop(q) #가장 최단 거리인 노드에 대한 정보 꺼내기

#         if distance[now] < dist:
#             continue

#         #현재 노드와 연결된 다른 인접한 노드 확인
#         for i in arr[now]: # (2, 2), (3, 3), (4, 1), (5, 10), (4, 2)
#             cost = dist + i[1]
            
#             #현재 노드를 거치면 이동 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
    
#     return distance

# for i in range(1, n+1):
#     dist = sol(i)

#     dist = [0 if j == 1e9 else j for j in dist[1:]]

#     print(*dist)

# 방법 2
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = []

INF = 1e9
cost = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            cost[i][j] = 0

for i in range(m):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())
    if cost[a][b] > c:
        cost[a][b] = c

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])

# print(cost)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j],end=' ')
    print()