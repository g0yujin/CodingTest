import sys

A, B, C, M = map(int, sys.stdin.readline().split())

cnt = 0

fatigue = 0

for i in range(24):
    if fatigue + A <= M: # 일 할 수 있는 경우
        fatigue += A
        cnt += 1
    elif fatigue + A > M:
        fatigue = max(0, fatigue - C)

print(cnt*B)