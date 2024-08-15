# import sys

# def check_bingo(bingoValue): # 3빙고인지 확인하는 함수
#     bingo= 0

#     bingoValueHorizontal = sorted(bingoValue)
#     bingoValueVertical = sorted(bingoValue, key=lambda x: x[1])

#     for i in range(0, 25, 5):
#         # 가로 빙고
#         if bingoValueHorizontal[i][2] == 1 and bingoValueHorizontal[i+1][2] == 1 and bingoValueHorizontal[i+2][2] == 1 and bingoValueHorizontal[i+3][2] == 1 and bingoValueHorizontal[i+4][2] == 1:
#             bingo += 1

#             # print(bingo , '가로 빙고')
#             if bingo >= 3:
#                 return True
        
#         # 세로 빙고
#         if bingoValueVertical[i][2] == 1 and bingoValueVertical[i+1][2] == 1 and bingoValueVertical[i+2][2] == 1 and bingoValueVertical[i+3][2] == 1 and bingoValueVertical[i+4][2] == 1:
#             bingo += 1

#             # print(bingo, '세로 빙고')
#             if bingo >= 3:
#                 return True
        
#     # 대각선 빙고
#     if bingoValue[0][2] == 1 and bingoValue[6][2] == 1 and bingoValue[12][2] == 1 and bingoValue[18][2] == 1 and bingoValue[24][2] == 1:
#         bingo += 1

#         # print(bingo, '대각선 빙고(↘)')
#         if bingo >= 3:
#             return True
        
#     if bingoValue[4][2] == 1 and bingoValue[8][2] == 1 and bingoValue[12][2] == 1 and bingoValue[16][2] == 1 and bingoValue[20][2] == 1:
#         bingo += 1

#         # print(bingo, '대각선 빙고(↗)')
#         if bingo >= 3:
#             return True

# bingo = {}
# cnt = 0

# for i in range(5):
#     oneline = list(map(int, sys.stdin.readline().split()))
    
#     for j in range(5):
#         bingo[oneline[j]] = [i, j, 0] # 안불린 상태 = 0

# # 빙고판 완성
# # print(bingo)

# for i in range(5):
#     num = list(map(int, sys.stdin.readline().split()))

#     for j in range(5):
#         bingo[num[j]][2] = 1 # 불린 상태 = 1
#         cnt += 1 # 부른 수
        
#         if check_bingo(list(bingo.values())): # 빙고가 완성되었는지 확인

#             minus = 6-i
#             break
    

# print(cnt-minus) # 빙고가 완성된 후에도 불린 수를 계속 세어서 빼줌


def check(tmp):
    # 가로
    for i in range(5):
        if bingo[i] == [0] * 5:
            tmp += 1
    # 세로
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            tmp += 1
    # 대각선1
    if all(bingo[i][i] == 0 for i in range(5)):
        tmp += 1
    # 대각선2
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        tmp += 1
    return tmp

bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                cnt += 1
    if cnt >= 12:
        result = check(tmp)
        if result >= 3:
            print(i + 1)  # 배열은 0 부터 시작했으므로 
            break