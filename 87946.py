def solution(startFatigue, dungeons):
    def recursion(depth, fatigue):
        global answer, isVisit

        if (depth > answer):  # 더 많은 던전을 탐험하였다면
            answer = depth  # 답 갱신

        for i, d in enumerate(dungeons):
            if (isVisit[i] == False):  # 방문하지않은 던전이고
                if (d[0] <= fatigue):  # 최소 필요 피로도보다 피로도가 많은 경우
                    fatigue -= d[1]  # 피로도 감소
                    isVisit[i] = True  # 방문 체크

                    recursion(depth + 1, fatigue)

                    isVisit[i] = False  # 방문 해제
                    fatigue += d[1]

        return 0

    global answer, isVisit

    answer = 0
    length = len(dungeons)

    for i, d in enumerate(dungeons):
        isVisit = [False for i in range(length)]
        fatigue = startFatigue

        if (d[0] <= fatigue):  # 최소 필요 피로도보다 피로도가 많을 경우
            fatigue -= d[1]  # 피로도 감소시키고
            isVisit[i] = True  # 방문 체크

            recursion(1, fatigue)

    return answer
