import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

no_set = set()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    no_set.add((a, b))
    no_set.add((b, a))  # 순서에 상관없으므로 둘 다 추가

# print(no_set)

result = 0
for i in combinations(range(1, N+1), 3): # 1 ~ N 까지 3개의 조합
    a, b, c = i
    # 세 개의 조합 중 두 개가 금지된 조합에 포함되는지 확인
    if (a, b) in no_set or (a, c) in no_set or (b, c) in no_set:
        continue
    result += 1 
print(result)