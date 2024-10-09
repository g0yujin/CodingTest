import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

arr = [[] for _ in range(V+1)]
#모든 간선 정보를 입력받기
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    
    arr[a].append((b, c))

inf = 1e9
distance = [inf] * (V+1)

def sol(start):

    q=[]    
    heapq.heappush(q, (0, start))
    
    distance[start] = 0

    while q:
        #가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        #현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드 확인
        for i in arr[now]: 
            cost = dist + i[1]
            
            #현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

sol(k)

# 출력
for i in range(1, V+1):

    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
