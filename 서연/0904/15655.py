# # 방법 1
# import sys
# from itertools import combinations

# N, M = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# for p in combinations(sorted(nums), M):
#     print(' '.join(map(str, p)))

# 방법 2
import sys

N, M = map(int, input().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
array = []

def backtracking(start):
    if len(array) == M:
        print(*array)
        return

    for i in range(start, N):
        if nums[i] not in array:
            array.append(nums[i])
            backtracking(i+1)
            array.pop()

backtracking(0)