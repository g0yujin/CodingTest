import sys

N, K = map(int, sys.stdin.readline().split())

value = [int(sys.stdin.readline().strip()) for _ in range(N)]

value.sort(reverse=True)

cnt = 0

for i in value:
    if K == 0:
        break
    cnt += K // i
    K %= i


print(cnt)