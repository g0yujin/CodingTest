import sys

N, K = map(int, sys.stdin.readline().split())

S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

P = [0] * N

for _ in range(K): # K번 반복
    for i in range(N):
        P[D[i]-1] = S[i]
    S = P.copy()
    
print(*P)