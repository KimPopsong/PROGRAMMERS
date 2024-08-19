from collections import deque


def solution(maps):
    avail = []
    maxWidth = len(maps[0])  # 가로 길이
    maxLength = len(maps)  # 세로 길이
    isVisit = [[False for i in range(maxWidth)] for i in range(maxLength)]  # 방문여부 체크

    def DFS(rr, cc):
        food = 0

        dfs = deque()
        dfs.append([rr, cc])
        isVisit[rr][cc] = True

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        while (len(dfs)):
            r, c = dfs.pop()

            food = food + int(maps[r][c])

            for i in range(4):
                if (0 <= int(r + dr[i]) < maxLength and 0 <= int(c + dc[i]) < maxWidth):
                    if (maps[r + dr[i]][c + dc[i]] != "X"):
                        if (isVisit[r + dr[i]][c + dc[i]] == False):
                            dfs.append([r + dr[i], c + dc[i]])
                            isVisit[r + dr[i]][c + dc[i]] = True

        return food

    for r in range(maxLength):
        for c in range(maxWidth):
            if (maps[r][c] != "X"):
                if (isVisit[r][c] == False):
                    avail.append(DFS(r, c))

    avail.sort()

    if (len(avail) == 0):
        avail.append(-1)

    return avail
