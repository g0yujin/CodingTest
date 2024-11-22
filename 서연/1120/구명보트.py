# def solution(people, limit):
#     answer = 0
#     people = sorted(people, reverse=True)
#     # print(people)
#     for i in people:
#         tot = i
#         if tot + people[-1] <= limit:
#             people.pop()
#         answer += 1
#     return answer

def solution(people, limit) :
    answer = 0
    people.sort()
    # print(people)

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer