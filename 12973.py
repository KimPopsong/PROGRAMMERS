from collections import deque


def solution(s):
    prev = s

    while (len(s)):
        check = deque()

        for c in s:
            if (len(check) == 0):
                top = ""

            else:
                top = check.pop()

            if (c == top):
                continue

            else:
                check.append(top)
                check.append(c)

        temp = ""
        for c in check:
            temp = temp + c

        s = temp

        if (prev == s):
            break

        else:
            prev = s

    if (len(s) == 0):
        return 1

    else:
        return 0
