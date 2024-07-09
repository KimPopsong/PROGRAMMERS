def solution(board):
    countO = 0
    countX = 0
    for i in range(3):  # X의 개수는 O보다 같거나 1 적어야함.
        for j in range(3):
            if (board[i][j] == 'O'):
                countO = countO + 1

            elif (board[i][j] == 'X'):
                countX = countX + 1

    if (countO - countX != 1 and countO - countX != 0):
        return 0

    flagO = False
    flagX = False

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == 'O'):
            flagO = True

        if (board[i][0] == board[i][1] == board[i][2] == 'X'):
            flagX = True

        if (board[0][i] == board[1][i] == board[2][i] == 'O'):
            flagO = True

        if (board[0][i] == board[1][i] == board[2][i] == 'X'):
            flagX = True

    if (board[0][0] == board[1][1] == board[2][2] == 'O'):
        flagO = True

    if (board[2][0] == board[1][1] == board[0][2] == 'O'):
        flagO = True

    if (board[0][0] == board[1][1] == board[2][2] == 'X'):
        flagX = True

    if (board[2][0] == board[1][1] == board[0][2] == 'X'):
        flagX = True

    if (flagO and flagX):  # 동시 승리 불가
        return 0

    if (flagO):  # O가 승리했는데 X의 개수보다 적을 수 없음
        if (countO <= countX):
            return 0
    
    if (flagX):  # X가 승리했는데 O의 개수가 X보다 많을 수 없음
        if (countO != countX):
            return 0

    return 1
