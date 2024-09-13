def solution(arr):
    def recursion(startR, startC, endR, endC):
        nod = arr[startR][startC]
        flag = False

        for r in range(startR, endR):  # 사각형 안에 모든 숫자가 같은지 확인
            for c in range(startC, endC):
                if (arr[r][c] != nod):
                    flag = True

                    break
            if (flag):
                break

        if (flag):  # 사각형 안에 모든 숫자가 같지 않다면, 4분면으로 나누어 재귀
            recursion(startR, (startC + endC) // 2, (startR + endR) // 2, endC)  # 1사분면
            recursion(startR, startC, (startR + endR) // 2, (startC + endC) // 2)  # 2사분면
            recursion((startR + endR) // 2, startC, endR, (startC + endC) // 2)  # 3사분면
            recursion((startR + endR) // 2, (startC + endC) // 2, endR, endC)  # 4사분면

        else:  # 사각형 안에 모든 숫자가 같다면
            for r in range(startR, endR):  # ""으로 치환
                for c in range(startC, endC):
                    arr[r][c] = ""
            arr[startR][startC] = nod  # 시작점에만 nod 추가

    size = len(arr)

    recursion(0, 0, size, size)

    countZero = 0
    countOne = 0

    for a in arr:
        countZero += a.count(0)
        countOne += a.count(1)

    return [countZero, countOne]
