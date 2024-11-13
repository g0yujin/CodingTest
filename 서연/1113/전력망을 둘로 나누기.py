# 방법 1
from collections import deque

def bfs(s, endPoint, n, graph):
        visited = [0] * (n+1)
        visited[s] = 1
        q = deque([s])

        cnt = 1

        while q:
            x = q.popleft()

            for node in graph[x]:
                if node != endPoint and visited[node] == 0:
                    q.append(node)
                    visited[node] = 1
                    cnt += 1
        return cnt
    
def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)

    for v in range(1, n + 1):
        for node in graph[v]:
            # print(v, node)
            a = bfs(v, node, n, graph)
            b = bfs(node, v, n, graph)
            answer = min(answer, abs(a-b))

    return answer

# # 방법 2
# from collections import defaultdict, deque

# def bfs(graph, start):
#     # print(graph)
#     visited = [start]
#     q = deque([start])
#     n = 1

#     while q:
#         node = q.popleft()

#         for x in graph[node]:
#             if x not in visited:
#                 visited.append(x)
#                 q.append(x)
#                 n += 1

#     return n


# def solution(n, wires):
#     answer = -1
    
#     arr = []

#     for i in wires:
#         graph = defaultdict(list) # defaultdict(<class 'list'>, {})
#         x, y = i
#         for j in wires:
#             if i == j:
#                 continue
#             a, b = j
#             graph[a].append(b)
#             graph[b].append(a)
        
#         # print(graph)
        
#         n1 = bfs(graph, x)
#         n2 = bfs(graph, y)

#         arr.append(abs(n1 - n2))

#     answer = min(arr)

#     return answer