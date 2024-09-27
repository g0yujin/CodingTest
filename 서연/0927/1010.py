# 시간 초과
# import sys
# from itertools import combinations

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split()) # N <= M
#     print(len(list(combinations(range(M), N))))


import sys

# import math -> math.factorial()과 같음
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split()) # N <= M
    print(factorial(M) // (factorial(M-N) * factorial(N)))

