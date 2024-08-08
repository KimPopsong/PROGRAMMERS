def solution(s):
    time = 0  # 반복 횟수
    erase = 0

    while (s != "1"):
        time = time + 1

        one = 0
        for c in s:
            if (c == "0"):
                erase = erase + 1

            else:
                one = one + 1

        s = str(bin(one)[2:])

    return [time, erase]
