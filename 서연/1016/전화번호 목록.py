# 방법 1
# def solution(phone_book):
#     phone_book = sorted(phone_book)
    
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
       
#     return True

# 방법 2 - hash의 정석
def solution(phone_book): 

    # 1.Hash map생성
    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != nums:       
                return False 
                
    return True

# # 3, 4 효율성 시간초과
# def solution(phone_book):
#     phone_book = sorted(phone_book)
    
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[j].find(phone_book[i]) == 0:
#                 return False
        
#     return True