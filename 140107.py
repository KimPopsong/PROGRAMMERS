import math


def solution(k, d):
    dots = d // k + 1

    for x in range(0, d + 1, k):  # X축을 기준으로 Y의 개수를 계산
        yMax = math.sqrt(d ** 2 - x ** 2)
        dots = dots + math.floor(yMax) // k

    return dots
