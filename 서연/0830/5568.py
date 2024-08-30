import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

strlist = []
for permu in permutations(nums, k):
    strlist.append(int(''.join(''.join(sublist) for sublist in permu)))

# print(strlist)

# 중복 제거
result = list(set(strlist))
# print(result)
print(len(result))