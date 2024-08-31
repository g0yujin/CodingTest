import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

like = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
for a, b, c in combinations(range(M), 3):
    sum = 0
    for i in range(N):
        sum += max(like[i][a], like[i][b], like[i][c])
    result = max(result, sum)

print(result)