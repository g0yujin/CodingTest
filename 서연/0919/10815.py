# # 방법 1
# import sys

# N = int(sys.stdin.readline())
# have = list(map(int, sys.stdin.readline().split()))

# M = int(sys.stdin.readline())
# guess = list(map(int, sys.stdin.readline().split()))

# dict = {}

# for i in range(len(have)):
#     dict[have[i]] = 0  # 아무 숫자로 mapping

# for j in range(M):
#     if guess[j] not in dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')

# # 방법 2
# import sys

# N = int(sys.stdin.readline())
# have = sorted(list(map(int, sys.stdin.readline().split())))

# M = int(sys.stdin.readline())
# guess = list(map(int, sys.stdin.readline().split()))

# for check in guess:
#     low, high = 0, N-1
#     exist = False

#     while low <= high:
#         mid = (low + high) // 2
#         if have[mid] > check:  # 중간 값보다 작다면
#             high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
#         elif have[mid] < check:  # 중간 값보다 크다면
#             low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
#         else:
#             exist = True
#             break

#     print(1 if exist else 0, end=' ')


# 방법 3
import sys
import bisect

N = int(sys.stdin.readline())
have = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
guess = list(map(int, sys.stdin.readline().split()))

answer = [0] * M
for i in guess:
    l = bisect.bisect_left(have, i)
    r = bisect.bisect_right(have, i)
    print(r - l, end=' ')