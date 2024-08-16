# import sys

# N = int(sys.stdin.readline()) # 5
# N2 = N*N # 25
# m = N // 2 # 2

# map = [[0] * N] * N # 5*5

# step = ['up', 'right', 'down', 'left']

# def updateMap(map, startPlace, startNum, step):
#     if step == 'up':
#         map[startPlace[0]-1][startPlace[1]] = startNum
#         startPlace[0] -= 1
#     elif step == 'right':
#         map[startPlace[0]][startPlace[1]+1] = startNum
#         startPlace[1] += 1
#     elif step == 'down':
#         map[startPlace[0]+1][startPlace[1]] = startNum
#         startPlace[0] += 1
#     elif step == 'left':
#         map[startPlace[0]][startPlace[1]-1] = startNum
#         startPlace[1] -= 1

# startPlace = [m, m]
# startStep = 0

# for i in range(1, N): # 1, 2, 3, 4
    
#     startNum = 1

#     if i != N-1: # 2번씩
#         for _ in range(2):
            
#             updateMap(map, startPlace, startNum, step[startStep]) 
#             print(map)
#             startNum += 1         
#             if startStep == 4:
#                 startStep = 0
#             else:
#                 startStep += 1
    
#     elif i == N-1: # 3번
#         for _ in range(3):
#             updateMap(map, startPlace, startNum, step[startStep]) 
#             print(map)       
#             startNum += 1  
#             if startStep == 4:
#                 startStep = 0
#             else:
#                 startStep += 1
    

    

# print(map)

n = int(input())
num = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 상, 우, 하, 좌 순서
graph = [[0]*n for _ in range(n)]
number = 2
x = n//2
y = n//2
graph[x][y] = 1
repeat = 1
i = 0 # dx,dy 가리키는 변수

answer = [x+1,y+1]
while x!=0 or y !=0:
   flag = 0
   for _ in range(2):
      for _ in range(repeat):
         x += dx[i]
         y += dy[i]
         graph[x][y] = number
         if number == num:  # 위치를 찾고자 하는 자연수이면 answer에 위치 저장
            answer = [x+1,y+1] 
         if x == 0 and y == 0: 
            flag = 1
            break
         number += 1
      if flag == 1: break
      i = (i+1)%4
   repeat += 1

for i in graph:
   print(*i)
   
print(*answer)