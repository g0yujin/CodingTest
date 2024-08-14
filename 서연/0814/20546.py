money = int(input())
stockPrice = list(map(int, input().split()))

# 초기 돈
junMoney = money
sungMoney = money

# 구매한 주식
junBuy = 0
sungBuy = 0

# 주가 변동 - 성민이 문제 풀 때만 사용
change = []

for i in range(13): # 0~12
    if stockPrice[i] < stockPrice[i + 1]:
        change.append('up')
    elif stockPrice[i] > stockPrice[i + 1]:
        change.append('down')
    else:
        change.append('same')

# 준현이
for i in stockPrice:
    if junMoney >= i:
        junBuy += junMoney // i
        junMoney %= i
    if junMoney == 0:
        break

jun = junMoney + junBuy * stockPrice[-1]

# 성민이
for i in range(11):
    if change[i] == 'up' and change[i + 1] == 'up' and change[i + 2] == 'up': # 매도
        if sungBuy == 0:
            continue
        else:
            sungMoney += sungBuy * stockPrice[i+3]
            sungBuy = 0

    elif change[i] == 'down' and change[i + 1] == 'down' and change[i + 2] == 'down': # 매수
        sungBuy += sungMoney // stockPrice[i+3]
        sungMoney %= stockPrice[i+3]

    else:
        continue

sung = sungMoney + sungBuy * stockPrice[-1]

# 최종 결과
if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")