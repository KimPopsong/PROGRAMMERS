from collections import deque


def solution(n, edge):
    answer = 0

    matrix = dict()

    for e in edge:  # 간선 표시
        e1, e2 = e
        e1 -= 1
        e2 -= 1

        if (e1 in matrix.keys()):
            matrix[e1].append(e2)

        else:
            matrix[e1] = [e2]

        if (e2 in matrix.keys()):
            matrix[e2].append(e1)

        else:
            matrix[e2] = [e1]

    isVisit = [False for i in range(n)]
    bfs = deque()
    bfs.append(0)
    isVisit[0] = True

    while (len(bfs)):
        answer = len(bfs)

        tempBfs = deque(bfs)
        bfs.clear()

        while (tempBfs):
            nod = tempBfs.popleft()

            for i in matrix[nod]:
                if (isVisit[i] == False):
                    bfs.append(i)
                    isVisit[i] = True

    return answer
