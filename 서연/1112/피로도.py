# # 방법 1
# def solution(k, dungeons):
#     answer = -1

#     def rec(c, k, ds):
#         nonlocal answer

#         for idx, d in enumerate(ds):
#             if k >= d[0]:
#                 nds = ds.copy()
#                 nds.pop(idx)
#                 # print(c + 1, k - d[1], nds)
#                 count = rec(c + 1, k - d[1], nds)
#                 if answer < count:
#                     answer = count
#         return c

#     rec(0, k, dungeons)

#     return answer

# # 방법 2
# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0

#     for order in permutations(range(len(dungeons))):
#         # print(order)
#         cur = k
#         local_ans = 0
#         for t in order:
#             require, consum = dungeons[t]
#             if cur >= require: # 현재 피로도가 최소 필요 필요도보다 크다면
#                 cur -= consum
#                 local_ans += 1
#         answer = max(answer, local_ans)

#     return answer

# 방법 3
answer = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(len(dungeons)):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global visited

    visited = [0] * len(dungeons)

    dfs(k, 0, dungeons)

    return answer