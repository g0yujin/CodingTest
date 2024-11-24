# # 방법 1
# def solution(d, budget):
#     answer = 0
#     d = sorted(d)

#     for i in d:
#         if budget - i >= 0:
#             answer += 1
#             budget -= i

#     return answer

# 방법 2
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
        # print(d)
    return len(d)