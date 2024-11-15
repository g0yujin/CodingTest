def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    
    for i in lost:
        arr[i-1] = 0
    
    for i in reserve:
        arr[i-1] += 1
    
    # print(arr)
    
    for i in range(n):
        if arr[i] == 0:
            if i == 0:
                if arr[i+1] == 2:
                    arr[i+1] = 1
                    arr[i] = 1
            elif i == n-1:
                if arr[i-1] == 2:
                    arr[i-1] = 1
                    arr[i] = 1
            else:    
                if arr[i-1] == 2:
                    arr[i-1] = 1
                    arr[i] = 1
                    continue
                elif arr[i+1] == 2:
                    arr[i+1] = 1
                    arr[i] = 1
                
    # print(arr)
    
    for i in arr:
        if i >= 1:
            answer += 1
    return answer

# # 방법 2
# def solution(n, lost, reserve):
#     real_lost = set(lost) - set(reserve)
#     real_reserve = set(reserve) - set(lost)
    
#     for student in real_reserve:
#         if student - 1 in real_lost:
#             real_lost.remove(student - 1)
#         elif student + 1 in real_lost:
#             real_lost.remove(student + 1)
    
#     return n - len(real_lost)
