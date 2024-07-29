def solution(answers):
    best = []

    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    right1 = 0
    right2 = 0
    right3 = 0

    for i in range(len(answers)):
        if (answers[i] == answer1[i % 5]):
            right1 = right1 + 1

        if (answers[i] == answer2[i % 8]):
            right2 = right2 + 1

        if (answers[i] == answer3[i % 10]):
            right3 = right3 + 1

    maxNum = max(right1, right2, right3)

    if (maxNum == right1):
        best.append(1)

    if (maxNum == right2):
        best.append(2)

    if (maxNum == right3):
        best.append(3)

    return best
