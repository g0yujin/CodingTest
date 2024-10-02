import sys

n = int(sys.stdin.readline())

scores = [0] + [int(sys.stdin.readline()) for _ in range(n)]

# print(scores)

dp = [0] * (n+1)

if n <= 2:
    print(sum(scores))
else:    
    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]
    # dp[3] = max(scores[1] + scores[3], scores[2] + scores[3])

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    
    print(dp[n])

'''
    n-2번째에서 올라온다면 n-2의 전체 값
    n-1번째에서 올라온다면 n-1의 (n-1)-2에서 올라온 것과 동일!
'''
