def solution(n):
    fib = []
    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n] % 1234567
