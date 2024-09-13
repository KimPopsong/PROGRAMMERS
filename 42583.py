from collections import deque
import copy


def solution(bridgeLength, weight, truckWeights):
    time = 0

    truckWeights = deque(truckWeights)
    crossTruck = deque()

    sumWeight = 0
    while (len(truckWeights) or len(crossTruck)):  # 모든 트럭이 다리를 건널때까지
        time += 1

        for truck in crossTruck:  # 다리를 건너는 트럭의 시간 증가
            truck[1] += 1

        for truck in copy.deepcopy(crossTruck):  # 다리를 다 건넜다면 트럭 삭제
            if (truck[1] > bridgeLength):
                sumWeight -= truck[0]
                crossTruck.popleft()

        if (sumWeight < weight and len(truckWeights) != 0):  # 트럭 무게의 합이 weight보다 작고, 대기중인 트럭이 있다면
            truck = truckWeights.popleft()

            if (sumWeight + truck > weight):  # 다리가 트럭 무게의 합을 못버틴다면
                truckWeights.appendleft(truck)  # 탈출

            else:  # 다리가 트럭 무게의 합을 버틴다면
                crossTruck.append([truck, 1])  # [트럭의 무게, 시간] 추가
                sumWeight += truck

    return time
