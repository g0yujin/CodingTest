import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(int(x), int(y))

# # 방법2
# for i in range(-999, 1000):
#     for j in range(-999, 1000):
#         if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
#             print(i, j)