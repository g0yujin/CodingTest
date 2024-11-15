# # 방법 1
# def solution(arr1, arr2):    
#     x = len(arr1)
#     y = len(arr1[0])
#     # print(x, y)
    
#     answer = [[0] * y for _ in range(x)]
    
#     for a in range(x):
#         for b in range(y):
#             # print(arr1[a][b] + arr2[a][b])
#             answer[a][b] = arr1[a][b] + arr2[a][b]
#     return answer

# # 방법 2
# def solution(arr1, arr2):
#     return [[c + d for c, d in zip(a,b)] for a, b in zip(arr1, arr2)]

# 방법 3
def solution(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]