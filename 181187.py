import math


def solution(r1, r2):
    dot = 0

    for x in range(1, r2 + 1):  # 1사분면 위의 점만 계산
        yMin = r1 * r1 - x * x  # y로 가능한 최소 값

        if (yMin <= 0):
            yMin = 0

        else:
            yMin = math.ceil(math.sqrt(yMin))

        yMax = math.floor(math.sqrt(r2 * r2 - x * x))  # y로 가능한 최대 값

        dot = dot + (yMax - yMin + 1)

    dot = dot * 4  # 한개 사분면 * 4

    return dot
