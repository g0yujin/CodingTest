from collections import deque

def solution(priorities, location):
    q = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    cnt = 0
    
    while q:
        current = q.popleft()
        
        # q안에 있는 것 중에서 우선순위가 높은 게 있다면
        if any(current[0] < item[0] for item in q): 
            q.append(current) # 다시 넣어
        else : # 뽑은 게 가장 높은 우선 순위라면
            cnt += 1
            if current[1] == location:
                return cnt