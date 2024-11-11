def solution(brown, yellow):
    answer = []
    a, b = 1, 1
    hap = (brown + 4) // 2
    
    for i in range(1, hap):
        b = i
        a = hap - i
        # print(a, b, (a-2) * (b-2))
        if (a-2) * (b-2) == yellow:
            return [a, b]
    return answer