import sys

N, M = map(int, sys.stdin.readline().split())
lights = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 1:
        lights[b-1] = c
        
    elif a == 2:
        for i in range(b-1, c):
            if lights[i] == 1:
                lights[i] = 0
            elif lights[i] == 0:
                lights[i] = 1
                
    elif a == 3:
        for i in range(b-1, c):
            lights[i] = 0
            
    elif a == 4:
        for i in range(b-1, c):
            lights[i] = 1
            
for i in lights:
    print(i, end=' ')            
        
   
# 한줄로 표현 가능
# print(*lights)