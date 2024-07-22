def solution(k, ranges):
    answer = []  # 답 저장

    dots = []  # 우박수열의 좌표 저장
    area = []  # 각각의 넓이 저장

    while (k > 1):  # 우박수열 계산
        dots.append(k)

        if (k % 2 == 0):
            k = k // 2

        else:
            k = k * 3 + 1
    dots.append(1)

    for i in range(len(dots) - 1):  # 1 단위로 넓이 계산
        h1 = max(dots[i], dots[i + 1])  # 높은 점
        h2 = min(dots[i], dots[i + 1])  # 낮은 점

        area.append((h1 + h2) / 2)

    for r in ranges:
        x, y = r

        sumTemp = 0

        if (x > len(dots) + y - 1):
            sumTemp = -1

        for i in range(x, len(dots) + y - 1):
            sumTemp = sumTemp + area[i]

        answer.append(sumTemp)

    return answer
