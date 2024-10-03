import sys

n = int(sys.stdin.readline()) # 계단의 개수

stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

d = [0] * (n+1)

d[1] = stairs[0]
d[n] = stairs[-1]

if n > 1:
    d[2] = stairs[0] + stairs[1]

for i in range(n+1, 3, -1):
    if i % 3 == 0:
        d[i] = max(d[i-1], d[i-2] + stairs[i-1])
    else:
        d[i] = d[i-1] + stairs[i-1]

print(d[n])