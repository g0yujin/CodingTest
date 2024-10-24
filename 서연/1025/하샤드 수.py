def solution(x):
    answer = True
    div = 0
    for i in str(x):
        div += int(i)
        
    if x % div == 0:
        return True
    return False