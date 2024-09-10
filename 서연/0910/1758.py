# # 시간 초과뜸
# import sys
# from itertools import permutations

# N = int(sys.stdin.readline())

# tips = [int(sys.stdin.readline()) for _ in range(N)]

# result = 0

# for i in permutations(tips):
#     tipsSum = 0

#     for idx, j in enumerate(i):
#         if j - idx > 0:
#             tipsSum += (j - idx)
#         else:
#             tipsSum += 0
    
#     result = max(result, tipsSum)

# print(result)

n = int(input())
tip_list = []
total = 0

for _ in range(n):
    tip = int(input())
    tip_list.append(tip)

tip_list.sort(reverse = True)

for i in range(len(tip_list)):
    give_tip = tip_list[i] - i
    if give_tip < 0:
        give_tip = 0
    total += give_tip

print(total)