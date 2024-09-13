import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

# # 방법 1
# result = arr[-1] + sum(arr[:-1])/2

# if int(result) == result:
#     print(int(result))
# else:
#     print(result)

# 방법 2
result = arr[-1]

for i in range(N-1):
    result += arr[i]/2

print(result)