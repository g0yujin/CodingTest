def solution(price, money, count):
    answer = 0
    tot = (price + price*count) / 2 * count
    answer = int(tot) - money
    if answer <= 0:
        answer = 0
    return answer