import sys

N, M = map(int, sys.stdin.readline().split())

dna_list = [list(sys.stdin.readline().strip()) for _ in range(N)]

result = ''
HammingDistance = 0

for i in range(M):
    dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for j in range(N):
        dna_dict[dna_list[j][i]] += 1
    
    dna_dict = sorted(dna_dict.items(), key = lambda x: (-x[1], x[0]))
    # print(dna_dict)

    result += dna_dict[0][0]
    HammingDistance += N - dna_dict[0][1]

print(result)
print(HammingDistance)