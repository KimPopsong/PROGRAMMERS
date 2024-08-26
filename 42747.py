def solution(citations):
    hIndex = 0

    citations.sort(reverse=True)  # 역방향 정렬

    if (sum(citations) == 0):
        return 0

    for hIndex in range(len(citations) - 1, -1, -1):
        if (citations[hIndex] >= hIndex + 1):
            break

    return hIndex + 1
