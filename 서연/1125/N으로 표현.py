def solution(N, number):
    s = [set() for x in range(8)]

    for idx, x in enumerate(s, start=1):
        x.add(int(str(N) * idx))
    print(s)  # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]

    # s[i] 즉 N을 i+1개 사용했을 때 만들 수 있는 숫자 구하기
    for i in range(len(s)):  # 0, 1, 2, 3, 4, 5, 6, 7
        for j in range(i):  # 1->0 / 2->0,1 / 3->0,1,2 / 4->0,1,2,3 / 5->0,1,2,3,4 / 6->0,1,2,3,4,5 / 7->0,1,2,3,4,5,6
            for op1 in s[j]:  # op1: N을 j+1번 사용하여 만들 수 있는 숫자들
                for op2 in s[i - j - 1]:  # op2: N을 i-j번 사용하여 만들 수 있는 숫자들
                    # op1과 op2를 사칙연산 --> 즉 N을 i+1번 사용하여 만들 수 있는 숫자를 구하게 되고 이를 s[i]에 대입
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:  # N을 i+1번 사용했을 때 찾고자하는 값 number가 존재한다면 i+1 return
            answer = i + 1
            break
        else:  # N을 8번 사용했는데도 찾고자하는 값 number가 존재하지 않는다면 -1 return
            answer = -1
    return answer