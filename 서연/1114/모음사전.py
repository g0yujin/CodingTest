# # 방법 1
# from itertools import product

# def solution(word):
#     lis = list()
#     words = ['A','E','I','O','U']
    
#     for j in range(1,6):
#         for i in product(words,repeat=j):
#             lis.append(list(i))
#     lis.sort()
    
#     # print(lis)

#     answer = 0
    
#     for i in lis :
#         # print(i)
#         answer += 1
#         st = ''.join(i)
#         # print(st)
#         if (st == word):
#             break
            
#     return answer

# # 방법 2
# def dfs(string, word, alphabets):
#     global answer 
#     answer += 1 

#     if string == word:
#         return True

#     if len(string) == 5:
#         return False

#     for alpha in alphabets:
#         if dfs(string + alpha, word, alphabets) == True:
#             return True
            
# def solution(word):
#     alphabets = ['A', 'E', 'I', 'O', 'U']
#     global answer 
#     answer = 0

#     for alpha in alphabets:
#         if dfs(alpha, word, alphabets) == True:
#             return answer

# 방법 3
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    position_weight = [781, 156, 31, 6, 1]
    result = 0

    for i, letter in enumerate(word):
        idx = vowels.index(letter)
        result += idx * position_weight[i] + 1
        # print(result)

    return result
