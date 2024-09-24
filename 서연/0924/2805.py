import sys

N, M = map(int, sys.stdin.readline().split()) # N: 나무 수, M: 상근이가 가져가려는 나무 길이

trees = sorted(list(map(int, sys.stdin.readline().split())))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in trees:
        if mid < i:
            sum += (i-mid)
    
    if sum >= M: # = 있어야 해..
        start = mid + 1
    else:
        end = mid - 1

print(end)