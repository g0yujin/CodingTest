import sys

n = int(sys.stdin.readline())

arr = [[0]*58 for _ in range(58)]

cnt = 0

for _ in range(n):
    a, b = map(str, sys.stdin.readline().strip().split(" => "))
    a, b = ord(a), ord(b)

    # print(a, b)
    if a == b:
        continue
    if not arr[a-65][b-65]:
        arr[a-65][b-65] = 1
        cnt += 1

# print(arr)

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and not arr[i][j] and arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                cnt += 1


# 출력
print(cnt)
for i in range(58):
    for j in range(58):
        if arr[i][j]:
            print(f"{chr(i+65)} => {chr(j+65)}")



# print(ord('A')) # 65 -> 0
# print(ord('Z')) # 90
# print(ord('a')) # 97
# print(ord('z')) # 122 -> 57