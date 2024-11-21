# # 방법 1
# def solution(routes):
#     # 진출지점에 대해서 오름차순 정렬
#     routes.sort(key=lambda x: x[1])
#     # 기준은 제한사항 참조
#     key = -30001
#     # 필요한 카메라 수
#     cnt = 0

#     for route in routes:
#         # 기준(카메라)보다 진입지점이 뒤에 있으면
#         if route[0] > key:
#             # 단속이 안되기에 카메라 하나 더 필요
#             cnt += 1
#             # 새로운 기준은 해당 경로의 진출지점(맨끝)
#             key = route[1]

#     return cnt

# 방법 2
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    # print(routes) # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    i = 0
    while i < len(routes):
        if i < len(routes):
            pos = routes[i][1]
        i += 1
        while i < len(routes) and routes[i][0] <= pos <= routes[i][1]:
            i += 1
        answer += 1

    return answer

