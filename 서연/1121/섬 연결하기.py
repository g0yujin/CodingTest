# # 방법 1
# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x: x[2]) 
#     link = set([costs[0][0]])

#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(link) != n:
#         for v in costs:
#             # 두 섬이 이미 더 낮은 가격으로 연결이 되었을 경우 무시
#             if v[0] in link and v[1] in link:
#                 continue
#             # 두 섬 중 하나가 연결이 되어있지 않을 때 비용을 더하기
#             if v[0] in link or v[1] in link:
#                 link.update([v[0], v[1]])
#                 answer += v[2]
#                 break

#     return answer

# # 방법 2
# import heapq

# def solution(n, costs):
#     answer = 0
#     from_to = [[] for _ in range(n)]
#     # print(from_to)
#     visited = [False] * n
#     q = []

#     for a, b, cost in costs:
#         from_to[a].append((b, cost))
#         from_to[b].append((a, cost))

#     # print(from_to)
#     '''
#     [
#         [(1, 1), (2, 2)], 
#         [(0, 1), (2, 5), (3, 1)], 
#         [(0, 2), (1, 5), (3, 8)], 
#         [(1, 1), (2, 8)]
#     ]
#     '''
#     heapq.heappush(q, (0, 0))

#     while False in visited:
#         cost, start = heapq.heappop(q)
#         if visited[start]: 
#             continue

#         visited[start] = True
#         answer += cost
#         for end, cost in from_to[start]:
#             if visited[end]: 
#                 continue
#             else:
#                 heapq.heappush(q, (cost, end))

#     return answer


# 방법 3
def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 건설 비용 기준 오름차순 정렬

    bridges = [i for i in range(n)]  # 연결된 섬: [0, 1, 2, 3]
    room = [[i] for i in range(n)]  # 섬에 연결된 섬들: [[0], [1], [2], [3]]

    answer = 0  # 건설 비용
    made = 0  # 만들어진 다리 개수

    for x, y, cost in costs:
        x = bridges[x]
        y = bridges[y]

        if x == y:
            continue

        # y 섬에 있는 섬들을 모두 x 섬으로 옮김
        while room[y]:
            k = room[y].pop()
            room[x].append(k)
            bridges[k] = x

        answer += cost
        made += 1

        if made == n - 1:
            break

    return answer