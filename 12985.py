def solution(n, a, b):
    def calcT(t):
        if (t % 2 == 1):
            t = t // 2 + 1

        else:
            t = t // 2

        return t

    match = 0

    if (a > b):  # 계산 편의를 위해 항상 b가 크도록
        a, b = b, a

    while (True):
        match = match + 1

        if (b % 2 == 0):
            if (b - 1 == a):
                break

            else:
                a = calcT(a)
                b = calcT(b)

        else:
            a = calcT(a)
            b = calcT(b)

    return match
