# 방법 1
T = int(input())

for _ in range(T):
    
    N = int(input())
    nlist = list(map(int, input().split()))
    nlist.sort()
    small = nlist[0]
    big = nlist[-1]
    print(small, big)

# # 방법 2
# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N = int(sys.stdin.readline())
#     number_list = sorted(map(int, sys.stdin.readline().split()))

#     print(number_list[0], number_list[-1])