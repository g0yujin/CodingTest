def solution(s):
    #     answer = ''

    #     idx = 0
    #     for i in s:
    #         if i == ' ':
    #             answer += ' '
    #             idx = 0
    #         else:
    #             idx += 1
    #             if idx % 2 == 1:
    #                 answer += i.upper()
    #             else:
    #                 answer += i.lower()

    #     return answer

    words = s.split(" ")
    lst = map(lambda x: "".join([a.lower() if idx % 2 else a.upper() for idx, a in enumerate(x)]), words)
    return " ".join(lst)