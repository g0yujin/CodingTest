import sys

def Clock(matrix, n):
    # newMatrix = [[0] * n] * n -> 이렇게 하면 동일 참조를 공유해서 문제가 발생함
    newMatrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if i == j: # 주대각선
                newMatrix[i][n//2] = matrix[i][j]

            elif i == n-j-1: # 부대각선
                newMatrix[n//2][j] = matrix[i][j]

            elif i == n//2: # 가운데 행
                newMatrix[j][j] = matrix[i][j]

            elif j == n//2: # 가운데 열
                newMatrix[i][n-i-1] = matrix[i][j]

            else:
                newMatrix[i][j] = matrix[i][j]
                
    return newMatrix

def antiClock(matrix, n):
    newMatrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if i == j: # 주대각선
                newMatrix[n//2][j] = matrix[i][j]

            elif i == n-j-1: # 부대각선
                newMatrix[i][n//2] = matrix[i][j]

            elif i == n//2: # 가운데 행
                newMatrix[n-j-1][j] = matrix[i][j]

            elif j == n//2: # 가운데 열
                newMatrix[i][i] = matrix[i][j]

            else:
                newMatrix[i][j] = matrix[i][j]
                
    return newMatrix

T = int(sys.stdin.readline().rstrip())

for _ in range(T): # T번 반복
    n, d = map(int, sys.stdin.readline().rstrip().split())
    
    matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    if d > 0:
        time = d // 45
        for _ in range(time):
            matrix = Clock(matrix, n)

    elif d < 0:
        time = abs(d) // 45
        for _ in range(time):
            matrix = antiClock(matrix, n)
    
    for i in matrix:
        print(*i)