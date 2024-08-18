# com = int(input())
# link = int(input())

# test = [[]]

# for i in range(link):
#     num1, num2 = map(int, input().split())
    
#     if i == 0:
#         test[0] = [num1, num2]

#     else:        
#         for j in range(len(test)):
#             if num1 in test[j] or num2 in test[j]:
#                 if num1 in test[j] and num2 in test[j]:
#                     continue
#                 elif num1 not in test[j]:
#                     test[j].append(num1)
#                 elif num2 not in test[j]:
#                     test[j].append(num2)
#             else:
#                 if j == len(test)-1:
#                     test.append([num1,num2])
#                     break
#                 else:
#                     continue

# danger = []

# for i in test:
#     if 1 in i:
#         for j in i:
#             danger.append(j)
            
# print(len(list(set(danger)))-1)

# DFS(깊이 우선 탐색)
com=int(input()) # 컴퓨터 개수
link=int(input()) # 연결선 개수

graph = [[] for i in range(com+1)] # 그래프 초기화

visited=[0]*(com+1) # 방문한 컴퓨터인지 표시

for i in range(link): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향

def dfs(link):
    visited[link]=1
    for nx in graph[link]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)