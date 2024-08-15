NUM = int(input())
state = list(map(int, input().split()))
student = int(input())

for i in range(student):
    gender, number = map(int, input().split())
    
    # 남자
    if gender == 1:
        for i in range(1, NUM+1):
            if i % number == 0:
                if state[i-1] == 1:
                    state[i-1] = 0
                else:
                    state[i-1] = 1
                    
    # 여자  
    else:
        switchindex = number - 1
        
        left = switchindex - 1
        right = switchindex + 1
        
        while True:
            
            if left < 0 or right > NUM-1:
                left += 1
                right -= 1
                break
                
            if state[left] == state[right]:
                left -= 1
                right += 1
            else:
                left += 1
                right -= 1
                break
                
        
        for i in range(left, right+1):
            if state[i] == 1:
                state[i] = 0
            else:
                state[i] = 1

result = ''.join(str(i) for i in state)

length = len(result)

# 20개씩 출력
if length>=20:
    for i in range((length)//20+1):
        start = int(i*20)
        print(' '.join(result[start:start+20]))
else:
    print(' '.join(result))                