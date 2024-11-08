import math

def solution(n):
    s = '수박'
    answer = s * math.ceil(n / 2)
    answer = answer[:n]
    return answer