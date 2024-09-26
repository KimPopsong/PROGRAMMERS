def solution(n, works):
    overtime = 0

    works.sort(reverse=True)
    while (n > 0 and sum(works) > 0):
        maxWork = works[0]  # 가장 큰 일

        for i, work in enumerate(works):
            if (n <= 0):
                break

            elif (work >= maxWork):
                works[i] -= 1
                n -= 1

            else:
                break

    for work in works:
        overtime += work ** 2

    return overtime
