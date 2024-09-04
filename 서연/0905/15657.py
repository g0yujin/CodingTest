import sys

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
array = []

def backtracking(start):
    if len(array) == M:
        print(*array)
        # print(' '.join(map(str, array)))
        return

    for i in range(start, N):
        array.append(nums[i])
        backtracking(i)
        array.pop()
    
backtracking(0)