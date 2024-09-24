import sys

K, N = map(int, sys.stdin.readline().split()) # K:오영식이 가지고 있는 개수, N: 원하는 길이

cables = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(cables)

result = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in cables:
        sum += (i // mid)
    
    # print(f'mid: {mid}, start: {start}, end: {end}일 때 {sum}')

    if sum >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

# print(result)
print(end)
