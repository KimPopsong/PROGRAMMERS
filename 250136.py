from collections import deque


def solution(land):
    oil = [0 for i in range(len(land[0]))]
    answer = 0

    for i in range(len(land)):
        for j in range(len(land[i])):
            if (land[i][j] == 1):
                startX, endX, oilSum = BFS(land, i, j)

                for n in range(startX, endX + 1):
                    oil[n] += oilSum

    for i in range(len(oil)):
        if oil[i] > answer:
            answer = oil[i]

    return answer


def BFS(land, i, j):
    oil = 0
    startX, endX = j, j

    bfs = deque()
    bfs.append([i, j])
    land[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while len(bfs):
        oil += 1
        tempI, tempJ = bfs.popleft()

        for n in range(4):
            if (tempI + dx[n] >= 0 and tempJ + dy[n] >= 0 and tempI + dx[n] < len(land) and tempJ + dy[n] < len(
                    land[0])):
                if (land[tempI + dx[n]][tempJ + dy[n]] == 1):
                    land[tempI + dx[n]][tempJ + dy[n]] = 0
                    bfs.append([tempI + dx[n], tempJ + dy[n]])

                    if (startX > tempJ + dy[n]):
                        startX = tempJ + dy[n]

                    if (endX < tempJ + dy[n]):
                        endX = tempJ + dy[n]

    return startX, endX, oil
