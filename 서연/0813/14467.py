# 방법 1
import sys

N = int(sys.stdin.readline())

dic = {}
cnt = 0
for _ in range(N):
    num, loc = map(int, sys.stdin.readline().split())
    try:
        if dic[num] != loc:
            dic[num] = loc
            cnt += 1
        else:
            pass
    except:
        dic[num] = loc

print(cnt)

# # 방법 2
# import sys

# N = int(sys.stdin.readline())

# dic = {}
# cnt = 0
# for _ in range(N):
#     num, loc = map(int, sys.stdin.readline().split())
#     if num not in dic:
#         dic[num] = loc
#     else:
#         if dic[num] != loc:
#             dic[num] = loc
#             cnt += 1

# print(cnt)