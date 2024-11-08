from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    lst = list(numbers)
    
    prime_number = []
    
    for i in range(1, len(lst)+1):
        for j in permutations(lst, i):
            num = int(''.join(j))
            # print(num)
            if isPrime(num):
                prime_number.append(num)
    # print(prime_number)            
    answer = len(set(prime_number))
    return answer
