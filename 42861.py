import heapq


def solution(n, costs):
    answer = 0

    matrix = [[False for i in range(n)] for i in range(n)]
    isVisit = [False for i in range(n)]

    for cost in costs:
        is1, is2, c = cost

        matrix[is1][is2] = c
        matrix[is2][is1] = c

    queue = [[0, 0]]  # [거리, 정점]
    heapq.heapify(queue)

    while (queue):
        distance, island = heapq.heappop(queue)

        if (isVisit[island] == True):  # 이미 방문한 섬일 경우 무시
            continue

        isVisit[island] = True

        answer += distance

        for index, land in enumerate(matrix[island]):
            if (land != False):  # 다리로 연결되어있고
                if (isVisit[index] == False):  # 가본적이 없는 섬이면
                    heapq.heappush(queue, [land, index])

    return answer
