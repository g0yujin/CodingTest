# def solution(n):
#     answer = list(map(int, reversed(str(n))))
    
#     return answer

def solution(n):
    return [int(i) for i in reversed(str(n))]

# def solution(n):
#     return [int(i) for i in str(n)][::-1]