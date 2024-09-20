import sys

N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# if M >= sum(budget):
#     print(max(budget))
# else:
#     for idx, money in enumerate(sorted(budget)):
#         if idx < N-1:
#             if M - money > sorted(budget)[idx+1]:
#                 M -= money
#             else: 
#                 print(M // (N-idx))


result = 0  # 출력해야 하는 최대 예산
start, end = 1, max(budget)

while start <= end:
    # print(start, end)
    mid = (start + end) // 2 
    total = 0

    for l in budget:
        if l > mid:
            total += mid
        else:
            total += l
    # print(total)

    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)