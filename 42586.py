from collections import deque


def solution(progresses, speeds):
    answer = []

    progress = deque()

    for i in range(len(speeds)):
        p = progresses[i]
        s = speeds[i]

        day = 0
        while (p < 100):
            day = day + 1
            p = p + s

        progress.append(day)

    while (len(progress)):
        release = 1

        nod = progress.popleft()

        while (len(progress)):
            temp = progress.popleft()

            if (temp <= nod):
                release = release + 1

            else:
                progress.appendleft(temp)

                break

        answer.append(release)

    return answer
