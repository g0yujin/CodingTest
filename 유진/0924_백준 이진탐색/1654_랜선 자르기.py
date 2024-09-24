import sys

K, N = map(int, sys.stdin.readline().split()) # 보유 랜선 개수, 필요 랜선 개수
lan = []
for i in range(K):
    lan.append(int(sys.stdin.readline()))


start = 1
end = max(lan)
length = []        # 랜선의 최대 길이

while start <= end:
    num = 0       # 랜선 개수
    mid = (start + end) // 2

    for i in lan:
        num += i // mid

    if num < N:

        end = mid - 1

    else:
        length.append(mid)
        start = mid + 1

print(max(length))



#start end  mid  num
#0     802   401  5
#0     400   200  11
#0      199   99  21
#100    199   149  16
#150    199   174  13



# 랜선의 길이를 이진탐색으로 구하기
# mid를 랜선의 길이로 잘랐을 때 랜선의 개수 구하기