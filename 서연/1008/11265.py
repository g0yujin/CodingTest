# import sys
# from collections import deque

# N, M = map(int, sys.stdin.readline().split())

# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > arr[i][k] + arr[k][j]:
#                 arr[i][j] = arr[i][k] + arr[k][j]

# for _ in range(M):
#     a, b, c = map(int, sys.stdin.readline().split())

#     result = arr[a-1][b-1] # 한번에 가는 시간

#     if result <= c:
#         print("Enjoy other party")
#     else:
#         print("Stay here")


import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

inf = 1e9

result = [[] for _ in range(N)]

def sol(a, b):
    if a == b: # 출발지와 도착지가 같음
        return 0

    # 최단 거리를 저장할 리스트
    dist = [inf] * N
    dist[a] = 0  # 시작점

    # 우선순위 큐
    q = []
    heapq.heappush(q, (0, a))  # 거리 0, 시작점
    
    while q:
        # 현재 가장 작은 비용과 그에 해당하는 파티장
        cost, now = heapq.heappop(q)
        
        # 만약 저장된 거리가 현재 비용보다 작으면 건너뜀
        if dist[now] < cost:
            continue
        
        # 현재 파티장에서 다른 모든 파티장으로의 이동 고려
        for next in range(N):
            tmp = cost + arr[now][next]
            
            # 만약 새로운 경로가 기존 경로보다 짧으면 갱신
            if tmp < dist[next]:
                dist[next] = tmp
                heapq.heappush(q, (tmp, next))  # 새로운 경로를 우선순위 큐에 추가
    
    result[a] = dist # 현재 파티장에서 다른 모든 파티장으로의 최단 경로 저장
    
    return dist[b] # 도착지까지의 최단 경로 반환


for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if result[a-1]:
        if result[a-1][b-1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")
    
    else: # 처음 계산하는 경우
        if sol(a-1, b-1) <= c:
            print("Enjoy other party")
        else:
            print("Stay here")