import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    result = i + num

    if result == n:
        print(i)
        break

    if i == n:  # 생성자가 없는 경우
        print(0)