import sys

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_price = price[0]
total = 0

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    total += min_price * length[i]
    
print(total)
