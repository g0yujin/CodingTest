import sys

N = int(sys.stdin.readline())  # 도시의 개수
road = list(map(int, sys.stdin.readline().split()))   # 도로의 길이
price = list(map(int, sys.stdin.readline().split()))  # 주유 가격

total = 0   # 총 주유 비용
now_cost = price[0]

for i in range(N-1):
    if price[i] <= now_cost:
        now_cost = price[i]
        total += now_cost * road[i]

    else:
        total += now_cost * road[i]

print(total)




