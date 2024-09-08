# # 방법 1
# import sys

# n = list(map(str, sys.stdin.readline().strip().split('.')))

# result = []

# for i in n:
#     if len(i) % 2 != 0:
#         print(-1)
#         exit()

#     a = len(i) // 4
#     b = len(i) % 4 // 2
#     result.append('AAAA' * a + 'BB' * b)

# print('.'.join(result))

# 방법 2
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)