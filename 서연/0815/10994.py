# 방법 1 - 일반항
# import sys

# n = int(sys.stdin.readline())

# n = (n-1)*4+1

# result = []

# # 절반만 찍기
# for i in range(n//2+1):
#     if i % 2 == 1:
#         result.append('* '*(i//2+1) + ' '*(n-(4*(i//2+1))) + ' *'*(i//2+1))

#     else:
#         result.append('* '*(i//2) + '*'*(n-i-2*(i//2)) + ' *'*(i//2))        

# # 절반 이후 뒤집어서 복사
# for i in range(n//2-1, -1, -1):
#     result.append(result[i])   

# # 출력
# for i in result:
#     print(i)

# 방법 2 - 재귀함수
n=int(input())
m=4*n-3

a=[[' ']*m for _ in range(m)]

def r(i):
    if i == m+1:
        return
    
    for j in range(i, m-i): 
        a[i][j], a[m-i-1][j]='*', '*'

    for j in range(i, m-i): 
        a[j][i], a[j][m-i-1]='*', '*'

    r(i+2)

r(0)

for i in a:
    print(*i,sep='')