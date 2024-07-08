from collections import deque


def solution(maps):
    row = len(maps)
    col = len(maps[0])

    time = 0
    flag = False  # 탈출 가능한 구조인지 확인
    visited = [[False] * col for _ in range(row)]

    startR, startC = 0, 0
    leverR, leverC = -1, -1

    for i in range(row):
        for j in range(col):
            if (maps[i][j] == 'S'):
                startR, startC = i, j
                break

    dfs = deque()
    dfs.append([startR, startC])
    visited[startR][startC] = True

    flag = True  # 레버를 찾을시 flag = False
    while (len(dfs) and flag):  # 레버 찾기
        time += 1

        tempQueue = dfs.copy()
        dfs.clear()

        while (len(tempQueue) and flag):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            t = tempQueue.pop()
            r = t[0]
            c = t[1]

            for i in range(4):
                if (r + dx[i] >= 0 and r + dx[i] < row and c + dy[i] >= 0 and c + dy[i] < col):  # 지도 범위 안에 있고
                    if (maps[r + dx[i]][c + dy[i]] != "X"):  # 지나갈 수 있는 길이며
                        if (not visited[r + dx[i]][c + dy[i]]):  # 방문하지 않은 길일 경우
                            dfs.append([r + dx[i], c + dy[i]])
                            visited[r + dx[i]][c + dy[i]] = True

                        if (maps[r + dx[i]][c + dy[i]] == 'L'):  # 만약 레버라면
                            leverR, leverC = r + dx[i], c + dy[i]
                            flag = False
                            break

    if (flag):  # 레버에 도달 불가능시
        return -1

    visited = [[False] * col for _ in range(row)]  # 다시 dfs를 해야하므로 초기화
    dfs.clear()
    dfs.append([leverR, leverC])
    visited[leverR][leverC] = True

    while (len(dfs)):  # 출구 찾기
        time += 1

        tempQueue = dfs.copy()
        dfs.clear()

        while (len(tempQueue)):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            t = tempQueue.pop()
            r = t[0]
            c = t[1]

            for i in range(4):
                if (r + dx[i] >= 0 and r + dx[i] < row and c + dy[i] >= 0 and c + dy[i] < col):  # 지도 범위 안에 있고
                    if (maps[r + dx[i]][c + dy[i]] != "X"):  # 지나갈 수 있는 길이며
                        if (not visited[r + dx[i]][c + dy[i]]):  # 방문하지 않은 길일 경우
                            dfs.append([r + dx[i], c + dy[i]])
                            visited[r + dx[i]][c + dy[i]] = True

                        if (maps[r + dx[i]][c + dy[i]] == 'E'):  # 만약 출구라면
                            return time

    return -1
