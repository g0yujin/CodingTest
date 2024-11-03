def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    
    if len(answer) == 0:
        answer = [-1]

    return answer