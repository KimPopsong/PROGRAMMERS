def solution(storey):
    magicStone = 0

    i = 1
    while (i < len(str(storey)) + 1):
        t = storey % pow(10, i) // pow(10, i - 1)

        if (t <= 4):
            magicStone = magicStone + t

        elif (6 <= t):
            magicStone = magicStone + (10 - t)
            storey = storey + pow(10, i)

        else:
            magicStone = magicStone + 5
            tt = storey % pow(10, i + 1) // pow(10, i)

            if (tt >= 5):
                storey = storey + pow(10, i)

        i = i + 1

    return magicStone
