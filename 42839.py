def solution(numbers):
    global isVisit, length, primes, number

    def recursion(depth, number):
        if (depth == length):
            if (erathos[int(number)]):  # 소수라면
                primes.add(int(number))  # 숫자 추가

            return 0

        for i in range(len(numbers)):
            if (isVisit[i] == False):
                isVisit[i] = True

                recursion(depth + 1, number + numbers[i])

                isVisit[i] = False

    erathos = [True for i in range(10000000)]  # 에라토스테네스의 채, 소수 먼저 구해두기

    erathos[0] = False
    erathos[1] = False

    for i in range(2, 5000001):
        if (erathos[i] == False):
            continue

        else:
            end = 10000000 // i

            for j in range(2, end):
                erathos[i * j] = False

    numbers = list(numbers)

    primes = set()

    for i in range(1, len(numbers) + 1):  # 자리수
        length = i

        for j in range(len(numbers)):  # 시작 숫자
            number = ""
            isVisit = [False for i in range(len(numbers))]

            number += numbers[j]
            isVisit[j] = True

            recursion(1, number)

    return len(primes)
