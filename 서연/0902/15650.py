# 방법 1
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

for i in combinations(range(1, N+1), M):
    print(' '.join(map(str, i)))

# # 방법 2
# import sys
# input = sys.stdin.readline

# def backtracking(start):
#     if len(array) == m:
#         print(" ".join(map(str, array)))
#         return

#     for i in range(start, n+1):
#         if i not in array:
#             array.append(i)
#             backtracking(i+1)
#             array.pop()

# n, m = map(int,input().split())
# array = []

# backtracking(1)