import sys

N, M = map(int, sys.stdin.readline().split()) #N: 입국심사대 수 M: 인원 수

T = [int(sys.stdin.readline()) for _ in range(N)]

start, end = min(T), max(T)*M

result = end
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in range(N):
        sum += mid // T[i]

    if sum >= M:
        end = mid - 1
        result = min(mid, result)
    else:
        start = mid + 1

print(result)