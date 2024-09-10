n = int(input())

w_list = []

total = 0

for _ in range(n):
    w = int(input())
    w_list.append(w)

w_list.sort()

result = []

for i in w_list:
    result.append(i * n)
    n -= 1

print(max(result))