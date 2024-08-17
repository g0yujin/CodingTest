import sys

S = sys.stdin.readline().rstrip() + ' '

tmp = []
check = False
result = ''

for i in S:
    if i == '<':
        check = True
        for j in range(len(tmp)): # <를 만나기 전에 저장된 것들을 뒤집어서 출력
            result += tmp.pop() 

    tmp.append(i)

    if i == '>':
        check = False
        for j in range(len(tmp)):
            result += tmp.pop(0)
    
    if i == ' ' and check == False:
        tmp.pop()
        for j in range(len(tmp)):
            result += tmp.pop()
        result += ' '

print(result)