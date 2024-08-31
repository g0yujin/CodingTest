import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
num = [sys.stdin.readline().strip()for _ in range(n)]
result = []

# 순열
for i in permutations(num,k):
    result.append("".join(i))

# 중복 제거
print(len(set(result)))