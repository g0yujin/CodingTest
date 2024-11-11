# def check(num):
#     result = 1
#     for i in range(1, num):
#         if num % i == 0:
#             result += 1
        
#     if result % 2 == 0:
#         return True
#     else:
#         return False

# def solution(left, right):
#     answer = 0
#     for i in range(left, right+1):
#         if check(i):
#             answer += i
#         else:
#             answer -= i
#     return answer


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer