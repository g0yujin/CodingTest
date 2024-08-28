import sys

A = int(sys.stdin.readline().strip())
T = int(sys.stdin.readline().strip())
check = int(sys.stdin.readline().strip())

beon = 1 # '번'을 외친 횟수
degi = 1 # '데기'를 외친 횟수

games = []

num = 0 # 몇 번째 게임인지

while True:
    cnt = beon

    num += 1

    for _ in range(2): # 처음은 번 데기 번 데기
        games.append([beon, 0])
        beon += 1
        games.append([degi, 1])
        degi += 1

    # 번
    for _ in range(num+1):
        games.append([beon, 0])
        beon += 1
    
    # 데기
    for _ in range(num+1):
        games.append([degi, 1])
        degi += 1

    if cnt <= T < beon:
        print(games.index([T, check]) % A)
        break