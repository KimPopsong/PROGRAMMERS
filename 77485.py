import copy


def solution(rows, columns, queries):
    answer = []

    matrix = []

    temp = []  # 행렬 채우기
    for i in range(1, rows * columns + 1):
        temp.append(i)

        if (i % columns == 0):
            matrix.append(copy.deepcopy(temp))
            temp.clear()

    for query in queries:
        startR, startC, endR, endC = query

        dr = [0, 1, 0, -1]  # 우, 하, 좌, 상 순으로 이동
        dc = [1, 0, -1, 0]

        movedNumber = []

        r, c = startR - 1, startC - 1
        nod = 0
        temp1 = matrix[r][c]
        temp2 = 0
        for turn in range((endR + endC - startR - startC) * 2):
            movedNumber.append(temp1)

            if (not (startR - 1 <= r + dr[nod] <= endR - 1) or not (
                    startC - 1 <= c + dc[nod] <= endC - 1)):  # 범위를 벗어난다면
                nod = nod + 1

                if (nod >= 4):
                    nod = 0

            temp2 = matrix[r + dr[nod]][c + dc[nod]]
            matrix[r + dr[nod]][c + dc[nod]] = temp1
            temp1 = temp2

            r = r + dr[nod]
            c = c + dc[nod]

        answer.append(min(movedNumber))

    return answer
