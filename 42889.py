def solution(N, stages):
    answer = []
    user = len(stages)
    challenger = [0] * (N + 2)
    clearUser = [0] * (N + 2)

    for i in range(0, user):
        challenger[stages[i]] += 1

        for j in range(0, stages[i] + 1):
            clearUser[j] += 1

    failPercent = []

    for i in range(1, N + 1):
        temp = []

        temp.append(i)
        
        if clearUser[i] == 0:
            temp.append(0)

        else:
            temp.append(challenger[i] / clearUser[i])

        failPercent.append(temp)

    failPercent = sorted(failPercent, key = lambda x: x[1], reverse=True)

    for i in range(N):
        answer.append(failPercent[i][0])
        
    return answer
