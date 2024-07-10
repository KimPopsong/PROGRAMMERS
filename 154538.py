from collections import deque
import copy


def solution(x, y, n):
    flag = True

    numbers = [1000001 for i in range(1000002)]

    dfs = deque()
    dfs.append(x)
    numbers[x] = 0  # 방문하는데 걸리는 시간 저장

    time = 0
    while (len(dfs)):
        time += 1

        tempDFS = copy.deepcopy(dfs)
        dfs.clear()

        while (len(tempDFS)):
            t = tempDFS.pop()

            if (t + n <= 1000000 and numbers[t + n] > time):
                dfs.append(t + n)
                numbers[t + n] = time

            if (t * 2 <= 1000000 and numbers[t * 2] > time):
                dfs.append(t * 2)
                numbers[t * 2] = time

            if (t * 3 <= 1000000 and numbers[t * 3] > time):
                dfs.append(t * 3)
                numbers[t * 3] = time

    if (numbers[y] == 1000001):
        return -1

    return numbers[y]
