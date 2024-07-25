from collections import Counter


def solution(want, number, discount):
    answer = 0
    wants = []

    for i in range(len(want)):
        for j in range(number[i]):
            wants.append(want[i])
    wants = Counter(wants)

    for i in range(0, len(discount) - 9):
        discounts = Counter(discount[i:i + 10])

        if (not (wants - discounts)):
            answer = answer + 1

    return answer
