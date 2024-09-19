import sys

S = int(sys.stdin.readline())

sum_list = []
result = 0
i = 1

while True:
    if i + 1 > S - (result+i):
        break

    result += i
    sum_list.append(i)
    i += 1

print(len(sum_list)+1)


# 1부터 +1씩 하면서 result에 더해주기 (result == S가 될 때까지)
# 더한 값은 sum_list에 넣어주기
# len(sum_list)가 최종 결과
# (1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+29 = 200)
# if i = 19일 때
# i + 1 > S - (result + i) 이면 앞으로 더해질 자연수는 1개이므로 break
# print(len(sum_list)+1)


# ----------------
# 다른 풀이
# 계속 i += 1씩 하면서 result에 더해주다가 result > sum가 되면 print(i-2)
# result == sum이면  print(i-1)