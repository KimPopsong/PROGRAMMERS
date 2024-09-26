from collections import deque


def solution(n, computers):
    networkNumber = 0

    isVisit = [False for i in range(n)]  # 탐색하지 않은 컴퓨터가 있는지 확인
    queue = deque()

    flag = True
    while (flag):
        if (len(queue) == 0):  # queue가 비었을 때
            flag = False

            for i in range(n):  # isVisit 확인
                if (isVisit[i] == False):  # 탐색하지 않은 컴퓨터가 있다면
                    queue.append(i)  # queue에 탐색할 컴퓨터를 넣고
                    networkNumber += 1  # 네트워크 개수 1 증가
                    flag = True
                    break  # 탈출

        while (len(queue)):
            computer = queue.popleft()

            isVisit[computer] = True  # 방문처리

            for i in range(n):
                if (computers[computer][i] == 1):  # 네트워크로 연결되어있다면
                    if (isVisit[i] == False):  # 방문하지 않았던 컴퓨터라면
                        queue.append(i)

    return networkNumber
