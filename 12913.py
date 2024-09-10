def solution(land):
    score = 0

    for i in range(1, len(land)):
        for j in range(4):
            temp = land[i - 1][0:j] + land[i - 1][j + 1:4]
            land[i][j] += max(temp)

    score = max(land[-1])

    return score
