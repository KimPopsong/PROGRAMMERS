def solution(n, t, m, p):
    def calcNDigit(n, d):  # N진수 구하기
        nDigit = ""

        while (n > 0):
            remain = n % d

            if (remain == 10):
                remain = 'A'

            elif (remain == 11):
                remain = 'B'

            elif (remain == 12):
                remain = 'C'

            elif (remain == 13):
                remain = 'D'

            elif (remain == 14):
                remain = 'E'

            elif (remain == 15):
                remain = 'F'

            else:
                remain = str(remain)

            nDigit = nDigit + remain
            n = n // d
        nDigit = nDigit[::-1]
        return nDigit

    answer = ''

    numbers = "0"

    for i in range(1, t * m + 1):
        numbers += calcNDigit(i, n)

    for i in range(t):
        answer += numbers[p - 1]
        p += m

    return answer
