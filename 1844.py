from collections import deque
import copy


def solution(maps):
    width = len(maps)  # 맵의 가로 길이
    length = len(maps[0])  # 맵의 세로 길이

    turn = 0
    isVisit = [[False for i in range(length)] for i in range(width)]
    dfs = deque()

    dfs.append([0, 0])  # Initialize
    isVisit[0][0] = True

    while (len(dfs)):
        turn = turn + 1

        tempDfs = copy.deepcopy(dfs)
        dfs.clear()

        while (len(tempDfs)):
            r, c = tempDfs.pop()

            if (r == width - 1 and c == length - 1):  # 목적지에 도착하였다면
                return turn  # 탈출

            dr = [1, -1, 0, 0]
            dc = [0, 0, 1, -1]

            for d in range(4):  # 상하좌우 길 탐색
                if (0 <= r + dr[d] < width and 0 <= c + dc[d] < length):  # 맵의 크기 안에 들어왔다면
                    if (maps[r + dr[d]][c + dc[d]] == 1 and isVisit[r + dr[d]][
                        c + dc[d]] == False):  # 벽이 아니거나 가봤던 길이 아니라면
                        isVisit[r + dr[d]][c + dc[d]] = True
                        dfs.append([r + dr[d], c + dc[d]])

    return -1
