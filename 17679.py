def solution(width, length, board):
    erase = 0

    for i in range(width):
        board[i] = list(board[i])

    while (True):
        isErase = [[False for i in range(length)] for i in range(width)]

        for r in range(width - 1):  # 2 X 2로 붙어있는 블록 찾기
            for c in range(length - 1):
                if (board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] != ""):
                    isErase[r][c] = True
                    isErase[r + 1][c] = True
                    isErase[r][c + 1] = True
                    isErase[r + 1][c + 1] = True

        for r in range(width):  # 블록 지우기
            for c in range(length):
                if (isErase[r][c]):
                    board[r][c] = ""

        flag = True  # 블록의 이동이 있는지 확인
        for r in range(width - 1, -1, -1):  # 블록 내리기
            for c in range(length - 1, -1, -1):  # 우측 하단부터, 좌측 상단 순
                if (board[r][c] == ""):
                    for rr in range(r - 1, -1, -1):
                        if (board[rr][c] != ""):  # 위에 문자가 있다면
                            board[r][c] = board[rr][c]  # 그 문자로 바꾸고
                            board[rr][c] = ""  # 바뀐 곳에 있던 문자는 NULL
                            flag = False
                            break

        if (flag):  # 아래로 내려간 블록이 없으면 탈출
            break

    for r in range(width):
        for c in range(length):
            if (board[r][c] == ""):
                erase += 1

    return erase
