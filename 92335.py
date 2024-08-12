import math


def solution(n, k):
    def CalcN(number, digit):
        string = ""

        while (number > 0):
            string = string + str(number % digit)
            number = number // digit
        string = string[::-1]

        return string

    def IsPrime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i == 0):
                return False

        return True

    primeCount = 0

    nDigit = CalcN(n, k).split("0")
    nDigit = [i for i in nDigit if i]  # 빈 원소 제거
    nDigit.sort()

    for num in nDigit:
        if (int(num) <= 1):
            continue

        if (IsPrime(int(num))):
            primeCount = primeCount + 1

    return primeCount
