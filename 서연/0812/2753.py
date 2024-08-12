import sys

year = int(sys.stdin.readline())

if (year % 400 == 0):
    print(1)
elif (year % 4 == 0) and (year % 100 != 0):
    print(1)
else:
    print(0)


# 한줄 방법
# print(1) if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else print(0)