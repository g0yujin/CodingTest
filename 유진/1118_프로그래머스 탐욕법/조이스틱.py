def solution(name):
    answer = 0
    n = len(name)
    min_moves = n - 1  # 기본 최소 이동횟수

    for i, char in enumerate(name):
        # 위/아래 조작 횟수
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 현재 위치 다음부터 연속된 A 찾기
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1

        # 세 가지 케이스 비교
        min_moves = min([
            min_moves,
            2 * i + n - next,  # 현재까지 왔다가 뒤로 가는 경우
            i + 2 * (n - next)  # 뒤로 갔다가 현재로 오는 경우
        ])

    return answer + min_moves