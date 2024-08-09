def solution(n):
    base124 = ""

    while (n > 0):
        mod = n % 3
        n = n // 3

        if (mod == 0):
            n = n - 1
            mod = 4

        base124 = base124 + str(mod)

    base124 = base124[::-1]  # 문자열 뒤집기

    return base124
