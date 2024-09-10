def solution(prices):
    answer = []

    for i in range(len(prices)):
        now = prices[i]

        for j in range(i + 1, len(prices)):
            if (prices[j] < now):
                break

        answer.append(j - i)

    return answer
