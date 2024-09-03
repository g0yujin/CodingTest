# # 방법 1
# import sys
# from itertools import permutations

# N, M = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# for p in permutations(sorted(nums), M):
#     print(' '.join(map(str, p)))

# 방법 2
import sys

N, M = map(int, input().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
array = []

def backtracking():
    if len(array) == M:
        # print(' '.join(map(str, array)))
        print(*array)
        return

    for i in range(N):
        if nums[i] not in array:
            array.append(nums[i])
            backtracking()
            array.pop()

backtracking()