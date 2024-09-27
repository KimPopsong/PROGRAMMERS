def solution(length, width, puddles):  # 가로, 세로, 물 웅덩이
    answer = 0

    dpMatrix = [[0 for i in range(length)] for i in range(width)]

    for i in range(length):  # 맨 윗 줄과
        dpMatrix[0][i] = 1

    for i in range(width):  # 맨 좌측 줄은 이동할 수 있는 방법이 1개밖에 없음
        dpMatrix[i][0] = 1

    for puddle in puddles:  # 물 웅덩이 표시
        c, r = puddle
        r -= 1
        c -= 1

        dpMatrix[r][c] = -1

        if (r == 0):  # 맨 윗 줄에 물 웅덩이가 있을 경우
            for i in range(c, length):
                dpMatrix[0][i] = 0

        if (c == 0):  # 맨 좌측 줄에 물 웅덩이가 있을 경우
            for i in range(r, width):
                dpMatrix[i][0] = 0

    for r in range(1, width):
        for c in range(1, length):
            if (dpMatrix[r][c] == -1):  # 물 웅덩이라면 넘어가기
                dpMatrix[r][c] = 0
                continue

            dpMatrix[r][c] = dpMatrix[r - 1][c] + dpMatrix[r][c - 1]

    answer = dpMatrix[width - 1][length - 1] % 1000000007

    return answer
