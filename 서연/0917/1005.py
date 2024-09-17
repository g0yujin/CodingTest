import sys
from collections import deque

T = int(sys.stdin.readline()) # 테스트 케이스의 개수

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split()) # N: 건물의 개수, K: 건물간의 건설 순서 규칙의 총 개수
    time = [0] + list(map(int, sys.stdin.readline().split())) # 각 건물당 건설에 걸리는 시간
    
    dp = [0] * (N+1) #해당 건물까지 걸리는 시간
    inDegree = [0] * (N+1) # 진입 차수
    graph = [[] for _ in range(N+1)] # 건물간의 건설 순서 규칙

    for _ in range(K): # 건설 순서 정리
        a, b = map(int, sys.stdin.readline().split()) 
        graph[a].append(b)
        inDegree[b] += 1
    
    # print(graph) # [[], [2, 3], [4], [4], []]
    # print(inDegree) # [0, 0, 1, 1, 2]

    q = deque()

    # 시작 점 찾기
    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    # print(q) # 1
    # print(dp) # [0, 10, 0, 0, 0]

    while q:
        tmp = q.popleft()

        for i in graph[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp]+time[i])
            if inDegree[i] == 0:
                q.append(i)
    
    W = int(sys.stdin.readline()) # 건설해야 할 건물의 번호
    print(dp[W])