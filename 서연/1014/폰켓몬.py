def solution(nums):
    answer = 0
    get = len(nums) // 2
    types = len(set(nums))
    
    # if get >= types:
    #     answer = types
    # else:
    #     answer = get
    
    answer = min(get, types)
        
    return answer