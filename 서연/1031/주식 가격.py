from collections import deque
def solution(prices):
    answer = []
    p = deque(prices)
    
    while p:
        a = p.popleft()
        tmp = 0
        for i in p:
            if a <= i:
                tmp += 1
            else:
                tmp += 1
                break
                
        answer.append(tmp)
    
    
    return answer