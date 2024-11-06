import math
def solution(answers):
    answer = []
    length = len(answers)
    
    a = [1, 2, 3, 4, 5] * math.ceil(length/5)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(length/8)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(length/10)
    
    aa, bb, cc = 0, 0, 0
    for i in range(length):
        if answers[i] == a[i]:
            aa += 1
        if answers[i] == b[i]:
            bb += 1
        if answers[i] == c[i]:
            cc += 1
            
    win = max(aa, bb, cc)
    
    if aa == win:
        answer.append(1)
    if bb == win:
        answer.append(2)
    if cc == win:
        answer.append(3)
    
    return answer