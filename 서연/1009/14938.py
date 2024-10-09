import sys
import heapq

n, m, r = map(int, sys.stdin.readline().split()) # 지역의 개수 n, 수색범위 m, 길의 개수 r

itemnums = list(map(int, sys.stdin.readline().split()))

arr = [ [] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())

    arr[a].append((b, l))
    arr[b].append((a, l))

# print(arr) # [[], [(4, 5), (2, 3)], [(5, 4), (3, 3), (1, 3)], [(2, 3)], [(1, 5)], [(2, 4)]]



result = [[]]

def sol(start):

    inf = 1e9
    distance = [inf] * (n+1)

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
    
    return distance

for i in range(1, n+1):
    result.append(sol(i))

# print(result) 
# [[], [1000000000.0, 0, 3, 6, 5, 7], [1000000000.0, 3, 0, 3, 8, 4], [1000000000.0, 6, 3, 0, 11, 7], [1000000000.0, 5, 8, 11, 0, 12], [1000000000.0, 7, 4, 7, 12, 0]]

total = 0
for i in range(1, n+1): # 1, 2, 3, 4, 5
    sum = itemnums[i-1]

    for idx, j in enumerate(result[i][1:]):
        # print(idx, j)
        if 0 < j <= m:
            sum += itemnums[idx]
    # print(sum)
    if sum > total:
        total = sum

print(total)