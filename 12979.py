import math


def solution(n, stations, w):
    stationNumber = 0

    apartment = []  # 기지국이 닿지 않는 아파트

    start = 1
    end = 1
    for s in stations:
        end = s - w - 1

        apartment.append([start, end])

        start = s + w + 1
    if (start <= n):
        apartment.append([start, n])

    for apt in apartment:
        start, end = apt

        stationNumber += math.ceil((end - start + 1) / (w * 2 + 1))

    return stationNumber
