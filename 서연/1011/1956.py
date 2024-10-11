# 메모리 초과
# import sys
# import heapq

# v, e = map(int, sys.stdin.readline().split())

# inf = 1e9
# arr = [[] for _ in range(v+1)]
# dist = [[inf] * (v+1) for _ in range(v+1)]

# q = []
# for _ in range(e):
#     a, b, c = map(int, sys.stdin.readline().split()) 

#     arr[a].append([c, b])
#     dist[a][b] = c
    
#     heapq.heappush(q, [c, a, b])

# while q:
#     cost, start, end = heapq.heappop(q)
    
#     # heap을 이용하기 때문에 처음 나온 사이클이 가장 비용이 작은 사이클이므로 break 해버려도 됨! -> 여기서 시간이 굉장히 절약되는 듯 
#     if start == end: # 출발지와 도착지가 같다면 사이클
#         print(cost)
#         break

#     if dist[start][end] < cost:
#         continue
        
#     for nd, newEnd in arr[end]:
        
#         new_d = cost + nd
        
#         if new_d < dist[start][newEnd]:
#             dist[start][newEnd] = new_d
#             heapq.heappush(q, [new_d, start, newEnd])

# else:   
#     print(-1) # heap 다 돌았는데 없다면 -1


import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())

dist = [[INF]*(v+1) for _ in range(v+1)]

heap = []
edge= [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c, = map(int, input().split())

    dist[a][b] = min(dist[a][b], c)

    edge[a].append([c, b])

    heapq.heappush(heap, [c, a, b])

while heap:

    w, s, g = heapq.heappop(heap)

    if s == g:
        print(w)
        break
    if w != dist[s][g]:
        continue
    for nw, ng in edge[g]:
        if dist[s][ng] > dist[s][g] + nw:
            dist[s][ng] = dist[s][g] + nw
            heapq.heappush(heap, [dist[s][ng], s, ng])

else:
    print(-1)
