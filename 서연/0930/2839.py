import sys
import math

num = int(sys.stdin.readline())

if num == 4:
    print(-1)
elif num == 7:
    print(-1)
else:
    if num % 5 == 2 or num % 5 == 4:
        print(math.ceil(num / 5) + 1)
    else:
        print(math.ceil(num / 5))


# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)