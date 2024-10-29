# # 방법 1
# import heapq

# def solution(jobs):
#     answer = 0
#     time = 0
#     n = len(jobs)

#     jobs.sort()
    
#     q = []
#     i = 0

#     while i < n or q:
#         while i < n and jobs[i][0] <= time:
#             heapq.heappush(q, (jobs[i][1], jobs[i][0]))
#             i += 1
#         if q:
#             duration, start = heapq.heappop(q)
#             answer += duration + time - start
#             time += duration
#         else:
#             time = jobs[i][0]

#     return answer // n

import heapq
from collections import deque

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)

    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))
    
    q = []
    
    while jobs or q:
        # 현재 시각(time)까지 도달 가능한 작업을 힙에 추가
        while jobs and jobs[0][0] <= time:
            start, duration = jobs.popleft()
            heapq.heappush(q, (duration, start))
        
        if q:
            # 가장 빨리 끝나는 작업을 꺼내 처리
            duration, start = heapq.heappop(q)
            time += duration
            answer += time - start
        else:
            # 다음 작업 시작 시각으로 time을 조정
            time = jobs[0][0]

    return answer // n