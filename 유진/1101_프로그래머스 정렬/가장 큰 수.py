'''  시간 초과

from itertools import permutations

def solution(numbers):
    answer = []
    for i in permutations(numbers, len(numbers)):
        temp = ''.join(map(str, i))
        answer.append(temp)


    answer.sort()
    return answer[-1]

'''


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)

    answer = ''.join(numbers)

    return str(int(answer))
