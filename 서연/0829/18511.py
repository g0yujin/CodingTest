import sys
from itertools import product # 중복순열

N, K = map(int, sys.stdin.readline().split())
K_list = list(map(int, sys.stdin.readline().split()))

num_list = []
for j in range(1, len(str(N))+1): # 모든 자리수 고려
    for i in product(K_list, repeat=j): # 중복순열 만들기
        num_list.append(int(''.join(map(str, i))))

max_num = 0

for i in num_list:
    if i > N:
        continue
    else:
        max_num = max(max_num, i)

print(max_num)

# 방법 2
# from itertools import product

# N,K = map(int,input().split())
# arr = list(map(str,input().split()))
# length = len(str(N))

# while(True):
#     temp = list(product(arr, repeat=length))
#     answer = []

#     for i in temp :
#         if int("".join(i)) <= N :
#             answer.append(int("".join(i)))

#     if len(answer)>= 1:
#         print(max(answer))
#         break
#     else : 
#         length -=1