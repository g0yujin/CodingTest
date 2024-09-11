n = int(input())
time= list((map(int, input().split())))
time = sorted(time)

result = 0
for i in range(n):
    time_hap = sum(time[:i+1])
    result += time_hap
    
print(result)        