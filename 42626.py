import heapq


def solution(scoville, K):
    mixTime = 0

    heapq.heapify(scoville)

    while (True):
        if (scoville[0] < K):  # 특정 음식이 스코빌 지수를 불만족시킬 때
            if (len(scoville) <= 1):  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 때
                return -1

            mixTime = mixTime + 1

            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1 + s2 * 2)

        elif (scoville[0] >= K):  # 모든 음식이 스코빌 지수를 만족시킬 때
            break

    return mixTime
