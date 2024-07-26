from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)  # list를 deque로
    queue2 = deque(queue2)

    target = (sum(queue1) + sum(queue2)) / 2
    time = 0

    sumQ1 = sum(queue1)  # 계산 최적화
    sumQ2 = sum(queue2)

    while (time <= (len(queue1) + len(queue2)) * 2):
        if (sumQ1 == target):
            break

        time = time + 1

        if (sumQ1 > target):
            sumQ1 = sumQ1 - queue1[0]
            sumQ2 = sumQ2 + queue1[0]
            queue2.append(queue1.popleft())

        else:
            sumQ1 = sumQ1 + queue2[0]
            sumQ2 = sumQ2 - queue2[0]
            queue1.append(queue2.popleft())

    if (time >= (len(queue1) + len(queue2)) * 2):
        return -1

    else:

        return time
