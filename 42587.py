from collections import deque
import heapq, copy


def solution(priorities, location):
    excuteTime = 0

    heap = []  # 최대 힙
    for item in priorities:
        heapq.heappush(heap, (-item, item))

    pQ = deque()

    for i in range(len(priorities)):  # [처음 위치, 우선순위] 큐
        pQ.append([i, priorities[i]])

    while (len(heap)):
        process = heapq.heappop(heap)[1]  # 실행해야하는 프로세스

        while (len(pQ)):
            p = pQ.popleft()

            if (p[1] == process):
                excuteTime = excuteTime + 1

                if (p[0] == location):
                    return excuteTime

                else:
                    break

            pQ.append(p)

    return excuteTime
