def solution(n):
    battery = 0

    while (n > 0):
        if (n % 2):  # 홀수
            n = n - 1
            battery = battery + 1

        else:
            n = n // 2

    return battery
