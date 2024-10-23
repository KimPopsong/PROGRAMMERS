def solution(n, k):
    answer = []

    factorial = [1 for i in range(21)]  # 팩토리얼 구하기
    for i in range(1, 21):
        factorial[i] = factorial[i - 1] * i

    numbers = [i for i in range(1, n + 1)]

    for i in range(n, 0, -1):
        digit = (k - 1) // factorial[i - 1]  # 들어갈 숫자 구하기

        answer.append(numbers[digit])
        numbers.pop(digit)

        k = k % factorial[i - 1]

    return answer
