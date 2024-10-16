def solution(clothes):
    dic = {}
    for name, typ in clothes:
        if typ in dic.keys():
            dic[typ] += 1
        else:
            dic[typ] = 1
    
    answer = 1
    for cnt in dic.values():
        answer *= (cnt+1)
        
    answer -= 1
    return answer