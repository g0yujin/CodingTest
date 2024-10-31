def solution(numbers):
    a = list(map(str, numbers))
    # print(a)
    a.sort(key = lambda x: x*3, reverse = True)
    # print(a)
    answer = str(int(''.join(a)))
    return answer