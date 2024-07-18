from collections import deque
import copy


def solution(board):
    startR = 0
    startC = 0

    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == "R"):
                startR, startC = i, j

    bfs = deque()
    move = -1  # 이동 횟수
    bfs.append([startR, startC])
    visited[startR][startC] = True
    flag = True  # 목표위치에 도달하였는지 여부

    while (len(bfs)):
        move = move + 1
        temp = copy.deepcopy(bfs)
        bfs.clear()

        for t in temp:  # 상하좌우 이동 가능한 위치를 탐색
            r, c = t

            if (board[r][c] == "G"):  # 목표위치 도달시
                flag = False
                bfs.clear()
                break

            tt = c
            while True:  # 왼쪽 탐색
                if (tt - 1 == -1 or board[r][tt - 1] == "D"):  # 왼쪽 벽을 넘어가거나 장애물일 때 현재 위치에서 정지
                    if (visited[r][tt]):  # 현재 위치가 이미 방문한 적이 있는 장소라면
                        break

                    else:  # 방문한적이 없다면
                        bfs.append([r, tt])
                        visited[r][tt] = True

                else:  # 아닐시 왼쪽으로 이동
                    tt = tt - 1

            tt = c
            while True:  # 오른쪽 탐색
                if (tt + 1 == len(board[0]) or board[r][tt + 1] == "D"):  # 오른쪽 벽을 넘어가거나 장애물일 때 현재 위치에서 정지
                    if (visited[r][tt]):  # 현재 위치가 이미 방문한 적이 있는 장소라면
                        break

                    else:  # 방문한적이 없다면
                        bfs.append([r, tt])
                        visited[r][tt] = True

                else:  # 아닐시 왼쪽으로 이동
                    tt = tt + 1

            tt = r
            while True:  # 위쪽 탐색
                if (tt - 1 == -1 or board[tt - 1][c] == "D"):  # 위쪽 벽을 넘어가거나 장애물일 때 현재 위치에서 정지
                    if (visited[tt][c]):  # 현재 위치가 이미 방문한 적이 있는 장소라면
                        break

                    else:  # 방문한적이 없다면
                        bfs.append([tt, c])
                        visited[tt][c] = True

                else:  # 아닐시 위로 이동
                    tt = tt - 1

            tt = r
            while True:  # 아래쪽 탐색
                if (tt + 1 == len(board) or board[tt + 1][c] == "D"):  # 아래쪽 벽을 넘어가거나 장애물일 때 현재 위치에서 정지
                    if (visited[tt][c]):  # 현재 위치가 이미 방문한 적이 있는 장소라면
                        break

                    else:  # 방문한적이 없다면
                        bfs.append([tt, c])
                        visited[tt][c] = True

                else:  # 아닐시 위로 이동
                    tt = tt + 1

    if (flag):  # 목표위치 도달 불가시
        return -1

    else:
        return move
