def solution(citations):
    citations = sorted(citations, reverse=True)
    # print(citations)
    for i in range(len(citations)):
        # print(citations[i], i + 1)
        if citations[i] < i + 1:            
            return i
    return len(citations)
    # print(map(min, enumerate(citations, start=1)))
    # return max(map(min, enumerate(citations, start=1)))