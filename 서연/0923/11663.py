import sys

N, M = map(int, sys.stdin.readline().split()) # 5 5

dots = sorted(list(map(int, sys.stdin.readline().split())))

# print(dots) # [1, 3, 10, 20, 30]

def dot_max(b): # 10
    start, end = 0, N-1 # 3, 2

    while start <= end:
        mid = (start + end) // 2 # 3

        if b < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end+1

def dot_min(a): # 1
    start, end = 0, N-1 # 0, -1
    
    while start <= end:
        mid = (start + end) // 2 # 0

        if dots[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end+1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split()) # 선분의 시작점과 끝점
    # print(dot_max(b), dot_min(a))
    print(dot_max(b) - dot_min(a))