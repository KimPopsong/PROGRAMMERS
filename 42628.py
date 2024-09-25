def solution(operations):
    answer = []

    numbers = []
    for op in operations:
        command, number = op.split()

        if (command == "I"):  # 숫자 삽입
            numbers.append(int(number))

        else:  # 숫자 제거
            numbers.sort()

            if (len(numbers) == 0):
                continue

            elif (number == "1"):  # 최댓값 삭제
                numbers.pop()

            else:  # 최솟값 삭제
                numbers.pop(0)

    if (len(numbers)):  # 큐가 비어있지 않다면
        answer = [max(numbers), min(numbers)]

    else:  # 큐가 비어있다면
        answer = [0, 0]

    return answer
