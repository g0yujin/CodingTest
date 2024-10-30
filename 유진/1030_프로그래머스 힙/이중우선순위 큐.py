import heapq


def solution(operations):
    heap = []
    answer = []

    for i in operations:
        start, end = i.split()

        # 숫자 삽입
        if start == "I":
            heapq.heappush(heap, int(end))

        else:
            if len(heap) == 0:
                pass
            elif end == "1":  # 최댓값 삭제
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

            else:  # 최솟값 삭제
                heapq.heappop(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer = [0, 0]

    return answer