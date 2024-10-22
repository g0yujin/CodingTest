import math

def solution(progresses, speeds):
    answer = []
    time = []
    for pro, spe in zip(progresses, speeds):
        time.append(math.ceil((100-pro) / spe))

    i = 1
    while True:
        if len(time) > i and time[0] >= time[i]:
            i += 1
            
        elif len(time) > i and time[0] < time[i]:
            answer.append(i)
            time = time[i:]
            i = 1
        else:
            answer.append(i)
            break
            
    return answer