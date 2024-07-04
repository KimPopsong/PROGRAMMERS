def solution(targets):
    answer = 0

    targets = sorted(targets, key=lambda x: x[1])

    i = 0
    flag = False
    while i < len(targets):
        end = targets[i][1]

        for j in range(i + 1, len(targets)):
            if targets[j][0] >= end:
                i = j - 1
                break

            elif j == len(targets) - 1:
                flag = True

        answer += 1
        i += 1

        if flag:
            break

    return answer
