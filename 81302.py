def solution(places):
    answer = []

    for place in places:
        isClose = [[0 for i in range(5)] for i in range(5)]

        for r in range(5):
            for c in range(5):
                if (place[r][c] == "P"):
                    isClose[r][c] = isClose[r][c] - 1
                    
                    dr = [1, -1, 0, 0]
                    dc = [0, 0, 1, -1]

                    for d in range(4):
                        if (0 <= r + dr[d] < 5 and 0 <= c + dc[d] < 5):
                            isClose[r + dr[d]][c + dc[d]] = isClose[r + dr[d]][c + dc[d]] - 1

                elif (place[r][c] == "X"):
                    isClose[r][c] = 100

        flag = False
        for r in range(5):
            for c in range(5):
                if (isClose[r][c] <= -2):
                    flag = True
                    break

        if (flag):
            answer.append(0)

        else:
            answer.append(1)

    return answer
