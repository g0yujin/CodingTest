def solution(s):
    # answer = ''
    # if len(s) % 2 == 1:
    #     sol = len(s)//2
    #     return s[sol]
    # else:
    #     sol1 = len(s)//2-1
    #     sol2 = len(s)//2
    #     return s[sol1] + s[sol2]
    
    return s[(len(s)-1)//2 : len(s)//2 + 1]