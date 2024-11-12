def solution(s):
    answer = ''
    s = list(s)
    # print(s)
    s = sorted(s, key=lambda x: -ord(x))
    # print(s)
    answer = ''.join(s)
    return answer
    # return ''.join(sorted(s, reverse=True))