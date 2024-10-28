from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
        
    while len(q) >= 2:
        a = heapq.heappop(q)
        
        if a >= K:
            break
            
        b = heapq.heappop(q)
        
        heapq.heappush(q, a+b*2)    
        answer += 1
    
    if q[0] >= K:
        return answer
    else:
        return -1