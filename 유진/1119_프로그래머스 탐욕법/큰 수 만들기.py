def solution(number, k):
    stack = []

    for num in number:
        # 스택이 비어있지 않고, k가 남아있고, 스택의 마지막 수가 현재 수보다 작으면 제거
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # k가 남아있다면 뒤에서 k개 제거
    stack = stack[:-k] if k > 0 else stack

    return ''.join(stack)