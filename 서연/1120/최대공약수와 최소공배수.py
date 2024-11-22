def solution(n, m):
    answer = []
    
#     # 최대공약수
#     for i in range(min(n, m), 0, -1):
#         if n % i == 0 and m % i == 0:
#             answer.append(i)
#             break
            
#     # 최소공배수
#     for i in range(1, n*m+1):
#         if i % n == 0 and i % m == 0:
#             answer.append(i)
#             break
    maxnum, minnum = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = maxnum % minnum
        maxnum, minnum = minnum, t
        # print(maxnum, minnum)
    answer = [ maxnum, int(n*m/maxnum)]
    return answer