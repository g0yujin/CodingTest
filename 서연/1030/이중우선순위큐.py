import heapq

def solution(operations):
    q = []
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(q, b)
        elif a == 'D':
            if b == -1 and q:
                heapq.heappop(q)
            elif b == 1 and q:
                q = q[:-1]
        
        # print(q)
    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]

# import heapq
# def solution(operations):
#     q = []
#     rq = []
#     for i in operations:
#         a, b = i.split()
#         b = int(b)
#         if a == 'I':
#             heapq.heappush(q, b)
#             heapq.heappush(rq, -b)
#         elif a == 'D':
#             if b == 1 and q:
#                 popped = heapq.heappop(rq)
#                 q.remove(-popped)
#             elif b == -1 and q:
#                 popped = heapq.heappop(q)
#                 rq.remove(-popped)
#         print(q)
#         print(rq)
#     if not q:
#         return [0,0]
#     else:
#         return [max(q), min(q)]