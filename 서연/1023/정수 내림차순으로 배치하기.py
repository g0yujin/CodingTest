def solution(n):
    answer = 0
    lst = sorted([int(i) for i in str(n)], reverse=True)
    # print(lst)
    newlst = [str(j) for j in lst]
    answer = int(''.join(newlst))
    return answer