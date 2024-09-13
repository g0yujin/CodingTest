# # 방법 1
# import sys

# N = int(sys.stdin.readline())   
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()

# result = 0

# if N % 2 == 0: # 짝수
#     tmp = []
#     for i in range(N//2):
#         tmp.append(arr[i] + arr[N-i-1])
#     result = max(tmp)
# else: # 홀수
#     tmp = []
#     for i in range(N//2):
#         tmp.append(arr[i] + arr[N-i-2])
#     tmp.append(arr[-1])
#     result = max(tmp)

# print(result)

# 방법 2
input()
a = [int(i) for i in input().split()]
a.sort()

m = 0
if len(a)%2 == 1:
    m = a.pop(-1)
    
b = [a[i] + a[-i-1] for i in range(len(a)//2)]
b.append(m)

print(max(b))