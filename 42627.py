import heapq, copy


def solution(jobs):
    processTime = 0

    jobs.sort()  # 작업이 들어온 순서대로 오름차순 정렬
    length = len(jobs)  # 작업의 개수

    canRun = []
    time = 0  # 처리할 작업이 없을 경우 생기는 공백 제거
    while (True):
        if (len(canRun) == 0):  # 작업이 없을 경우
            if (len(jobs) == 0):  # 모든 작업을 마쳤을 경우
                break  # 종료

            else:  # 가장 먼저 요청이 들어온 작업 넣어주기
                heapq.heappush(canRun, (jobs[0][1], jobs[0][0]))
                time = jobs[0][0]
                jobs.pop(0)

        runProcess = heapq.heappop(canRun)

        processTime += (time - runProcess[1]) + runProcess[0]  # 작업 시간 계산
        time += runProcess[0]

        for job in copy.deepcopy(jobs):  # 가능한 작업들의 목록 구하기
            requestTime, runningTime = job

            if (requestTime <= time):  # 실행이 가능한 상태라면
                heapq.heappush(canRun, (runningTime, requestTime))  # (작업의 소요시간, 작업이 요청되는 시점)으로 저장
                jobs.pop(0)

    return processTime // length
