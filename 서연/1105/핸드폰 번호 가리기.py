def solution(phone_number):
    answer = ''
    # star = len(phone_number[:-4])
    star = len(phone_number)-4
    answer = '*'*star + phone_number[-4:]
    return answer