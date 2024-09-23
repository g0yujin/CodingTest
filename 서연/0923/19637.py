import sys

N, M = map(int, sys.stdin.readline().split())

# 시간초과
# dic = {}

# for i in range(N):
#     word, level = map(str, sys.stdin.readline().split())
#     level = int(level)

#     if i == 0:
#         dic[word] = [0, level]
#     else:
#         dic[word] = [tmp+1, level]
    
#     tmp = level

# for _ in range(M):
#     inputlevel = int(sys.stdin.readline())

#     for word, level in list(dic.items()):
#         if level[0] <= inputlevel and inputlevel <= level[1]:
#             print(word)
#         else:
#             pass

dic = {}
for i in range(N):
    word, level = sys.stdin.readline().split()
    dic[i] = int(level), word

# print(dic) # {0: (10000, 'WEAK'), 1: (100000, 'NORMAL'), 2: (1000000, 'STRONG')}

def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2 

        if array[mid][0] >= target: #범위에 맞는 경우
            end = mid - 1
        else:
            start = mid + 1
    return array[start][1]

for j in range(M):
    inputlevel = int(sys.stdin.readline())
    result = binary_search(dic, inputlevel, 0, N-1)
    print(result)