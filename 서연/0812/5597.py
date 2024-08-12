# 방법 1
import sys

studentId = []
for _ in range(28):
    studentId.extend(list(map(int, sys.stdin.readline().split())))

notin = []

for i in range(1, 31):
    if i not in studentId:
        notin.append(i)
        
    if len(notin) == 2:
        break

print(notin[0])
print(notin[1])

# # 방법 2
# students = [i for i in range(1,31)]

# for _ in range(28):
#     applied = int(input())
#     students.remove(applied) #소거

# print(min(students))
# print(max(students))