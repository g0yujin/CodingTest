# # 방법 1
# import sys
# from itertools import product

# N, M = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# for i in product(sorted(nums), repeat=M):
#     print(' '.join(map(str, i)))

# 방법 2
import sys

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

array = []

def dfs():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    
    for i in range(N):
        array.append(nums[i])
        dfs()
        array.pop()

dfs()