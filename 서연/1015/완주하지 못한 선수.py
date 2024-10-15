# def solution(participant, completion):
    
#     dic = {}
    
#     for person in participant:
#         if person not in dic:
#             dic[person] = 1
#         else:
#             dic[person] += 1
            
#     for person in completion:
#         if person in dic:
#             dic[person] -= 1
            
#     for person in dic:
#         if dic[person] == 1:
#             return person

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
