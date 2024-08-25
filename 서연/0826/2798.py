import sys

N, M = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if sum < card[i] + card[j] + card[k] and card[i] + card[j] + card[k] <= M:
                sum = card[i] + card[j] + card[k]

print(sum)

# # 방법 2
# from itertools import combinations
 
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# result = 0
 
# for three in combinations(lst, 3):
#     if sum(three) <= M:
#         result = max(result, sum(three))
# print(result)