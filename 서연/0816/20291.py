import sys

n = int(sys.stdin.readline())

files = []
extensions = {}

for i in range(n):
    file = sys.stdin.readline().rstrip().split('.')
    extension = file[-1]
    if extension not in extensions.keys():
        extensions[extension] = 0
    files.append(file)

# files = sorted(files, key=lambda x: (x[1], x[0]))
# extensions.sort()

for i in files:
    extensions[i[1]] += 1

result = sorted(extensions.items(), key = lambda x: x[0])

for i in result:
    print(i[0], i[1])

# # 다른 풀이
# import sys

# n = int(sys.stdin.readline())

# file = dict()
# for _ in range(n):
#     extend = (sys.stdin.readline().split('.'))[1]
#     if not extend in file:
#         file[extend] = 1
#     else:
#         file[extend] += 1

# sort_file = sorted(file.items())

# for key, value in sort_file:
#     print(key.rstrip(), value)