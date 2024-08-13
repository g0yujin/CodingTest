import sys

number8 = '0o' + sys.stdin.readline()
number10 = int(number8, 8)

print(bin(number10)[2:])
# print(format(number10, 'b'))

# 한줄로
# print(bin(int(input(), 8))[2:])