def solution(sizes):
    answer = 0
    a, b = 0, 0
    for i, j in sizes:
        if i >= j:
            if i >= a:
                a = i
            
            if j >= b:
                b = j
        else:
            if j >= a:
                a = j
            
            if i >= b:
                b = i

    answer = a*b
        
    return answer