def solution(board):
    global boardWidth  # 가로 길이
    global boardLength  # 세로 길이
    maxLength = 0

    boardWidth = len(board[0])
    boardLength = len(board)

    for r in range(1, boardLength):
        for c in range(1, boardWidth):
            if (board[r][c] == 1):  # 위, 왼쪽, 왼쪽위 방향 중 최솟값 + 1 저장
                board[r][c] = min(min(board[r - 1][c], board[r][c - 1]), board[r - 1][c - 1]) + 1

    maxLength = max(map(max, board))

    return maxLength ** 2
