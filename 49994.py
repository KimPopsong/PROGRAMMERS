def solution(dirs):
    move1 = set()  # {출발(r, c), 도착(r, c)}
    move2 = set()  # {도착(r, c), 출발(r, c)}

    r, c = 0, 0  # 시작 좌표

    for i in dirs:
        startR, startC = r, c

        if (i == "U"):  # 위로
            r -= 1

            if (r < -5):
                r = -5

        elif (i == "D"):  # 아래로
            r += 1

            if (r > 5):
                r = 5

        elif (i == "R"):  # 오른쪽으로
            c += 1

            if (c > 5):
                c = 5

        else:  # 왼쪽으로
            c -= 1

            if (c < -5):
                c = -5

        if (startR == r and startC == c):
            continue

        else:
            m1 = (startR, startC, r, c)
            m2 = (r, c, startR, startC)

            if (m1 in move1 or m1 in move2):
                continue

            if (m2 in move1 or m2 in move2):
                continue

            move1.add(m1)
            move2.add(m2)

    return len(move1)
