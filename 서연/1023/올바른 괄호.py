# # 방법 1
# from collections import Counter

# def solution(s):
#     cnt = 0
    
#     a = Counter(s)
#     if a['('] != a[')']:
#         return False
#     else:
#         for i in s:
#             if cnt == 0 and i == ')':
#                 return False

#             elif i == '(':
#                 cnt += 1
#             elif i == ')':
#                 cnt -= 1

#         if cnt == 0:
#             return True
#         else:
#             return False
        
# # 방법 2
# def solution(s):

#     cnt = 0
#     for i in s:
#         if cnt < 0:
#             return False
#         if i == '(':
#             cnt += 1
#         else:
#             cnt -= 1

#     if cnt != 0:
#         return False

#     return True

# 방법 3
def solution(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0