def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 건설 비용 기준 오름차순 정렬

    bridges = [i for i in range(n)]  # 연결된 섬 (parents)
    room = [[i] for i in range(n)]  # 섬에 연결된 섬들

    answer = 0  # 건설 비용
    made = 0  # 만들어진 다리 개수

    for x, y, cost in costs:
        x = bridges[x]
        y = bridges[y]

        if x == y: continue

        # y 섬에 있는 섬들을 모두 x 섬으로 옮김
        while room[y]:
            k = room[y].pop()
            room[x].append(k)
            bridges[k] = x

        answer += cost
        made += 1

        if made == n - 1:
            break

    return answer
