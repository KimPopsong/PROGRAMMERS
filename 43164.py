import copy


def solution(tickets):
    def search(length, startPort):
        if (length == len(tickets)):
            avail.append(copy.deepcopy(orders))
            
            return 0

        for i in range(len(tickets)):
            if (tickets[i][0] == startPort):
                if (isVisit[i] == False):
                    isVisit[i] = True
                    orders.append(tickets[i][1])

                    search(length + 1, tickets[i][1])

                    isVisit[i] = False
                    orders.pop()

        return 0

    global avail, isVisit
    avail = []  # 가능한 모든 답안을 저장
    isVisit = [False for i in range(len(tickets))]  # 방문여부 확인

    for i in range(len(tickets)):
        global orders
        orders = ["ICN"]  # 방문 지역의 순서 저장

        if (tickets[i][0] == "ICN"):
            isVisit[i] = True
            orders.append(tickets[i][1])

            search(1, tickets[i][1])  # 탐색

            isVisit[i] = False

        orders.clear()

    avail.sort()
    return avail[0]
