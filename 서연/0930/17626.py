import sys
import math

n = int(sys.stdin.readline())

def solution(n):
    if int(math.sqrt(n)) == math.sqrt(n): # 제곱수
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2

    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
            
    return 4

print(solution(n))




# 1 = 1*1                         -> 1 # 1
# 2 = 1*1 + 1*1                   -> 2 # 1
# 3 = 1*1 + 1*1 + 1*1             -> 3 # 1

# 4 = 2*2                         -> 1 # 1, 2
# 5 = 2*2 + 1*1                   -> 2 # 1, 2
# 6 = 2*2 + 1*1 + 1*1             -> 3 # 1, 2
# 7 = 2*2 + 1*1 + 1*1 + 1*1       -> 4 # 1, 2
# 8 = 2*2 + 2*2                   -> 2 # 1, 2

#  9 = 3*3                        -> 1 # 1, 2, 3
# 10 = 3*3 + 1*1                  -> 2
# 11 = 3*3 + 1*1 + 1*1            -> 3
# 12 = 2*2 + 2*2 + 2*2            -> 3
# 13 = 3*3 + 2*2                  -> 2
# 14 = 3*3 + 2*2 + 1*1            -> 3
# 15 = 3*3 + 2*2 + 1*1 + 1*1      -> 4

# 16 = 4*4                        -> 1
# 17 = 4*4 + 1*1                  -> 2

