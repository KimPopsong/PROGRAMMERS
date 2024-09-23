import sys, heapq


def solution(villageNum, roads, deliverTime):
    answer = 0

    villages = [[sys.maxsize for i in range(villageNum)] for i in range(villageNum)]

    for road in roads:
        v1, v2, time = road
        v1 -= 1  # index = 마을번호 - 1
        v2 -= 1

        if (villages[v1][v2] != -1):  # 이미 할당된 이동 시간이 있다면
            if (villages[v1][v2] > time):  # 이미 할당된 이동 시간이 더 크다면 교체
                villages[v1][v2] = time
                villages[v2][v1] = time

        else:  # 이동 시간 추가
            villages[v1][v2] = time
            villages[v2][v1] = time

    heap = []
    heapq.heappush(heap, [0, 0])
    isVisit = [False for i in range(villageNum)]
    while (len(heap)):
        weight, village = heapq.heappop(heap)

        isVisit[village] = True

        if (villages[0][village] > weight):  # 거리가 더 짧다면 갱신
            villages[0][village] = weight

        for i in range(villageNum):
            if (isVisit[i]):  # 방문한 노드라면 통과
                continue

            else:
                if (villages[village][i] != sys.maxsize):
                    heapq.heappush(heap, [weight + villages[village][i], i])

    for i in range(villageNum):
        if (villages[0][i] <= deliverTime):
            answer = answer + 1

    return answer
