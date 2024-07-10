def solution(numbers):
    answer = []
    stack = []

    for i in range(len(numbers) - 1, -1, -1):  # 뒤에서부터 앞으로 비교
        flag = True

        for j in range(len(stack)):
            t = stack.pop()

            if (numbers[i] < t):
                answer.append(t)
                stack.append(t)
                stack.append(numbers[i])
                flag = False
                break

        if (flag):  # 보다 큰 수가 없으면
            answer.append(-1)
            stack.clear()
            stack.append(numbers[i])

    answer.reverse()

    return answer
