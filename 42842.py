def solution(brown, yellow):
    length = 0  # 가로
    width = 0  # 세로

    for i in range(1, yellow + 1):
        if (yellow % i != 0):  # 나누어 떨어지지 않는다면
            continue

        x = i
        y = yellow // i

        if (x * y + 2 * (x + y) + 4 == (brown + yellow)):
            width = x + 2
            length = y + 2

            break

    return [length, width]
