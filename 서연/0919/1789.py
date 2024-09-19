import sys

N = int(sys.stdin.readline())

num = 1
result = 0

while True:
    result += 1
    N -= num
    num += 1
    
    if N < num:
        break

print(result)