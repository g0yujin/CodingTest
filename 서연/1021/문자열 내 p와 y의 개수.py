def solution(s):
    s = s.lower()
    pcount = s.count('p')
    ycount = s.count('y')
    # if pcount == 0 and ycount == 0:
    #     return True
    
    if pcount == ycount:
        return True
    
    return False