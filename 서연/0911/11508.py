import sys

N = int(sys.stdin.readline())

arr = [ int(sys.stdin.readline()) for _ in range(N) ]

arr.sort(reverse=True)

result = 0
for i in range(0, N, 3):
    # print(i)
    # print(arr[i:i+3])
    if i+2 < N:
        result += arr[i] + arr[i+1]
    else:
        if i+1 < N:
            result += arr[i] + arr[i+1]
        else:
            result += arr[i]

print(result)