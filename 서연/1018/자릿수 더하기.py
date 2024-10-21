# def solution(n):    
#     n = str(n)
    
#     answer = 0
#     for i in n:
#         answer += int(i)

#     return answer

def solution(n):
    return sum(map(int, str(n)))