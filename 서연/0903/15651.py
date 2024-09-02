# 방법 1
import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

for i in product(range(1, N+1), repeat=M):
    print(' '.join(map(str, i)))

# # 방법 2
# import sys
# input = sys.stdin.readline

# def backtracking():
#     if len(array) == m:
#         print(" ".join(map(str, array)))
#         return

#     for i in range(1, n+1):
#         array.append(i)
#         backtracking()
#         array.pop()

# n, m = map(int,input().split())
# array = []

# backtracking()