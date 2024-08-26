def solution(orders, course):
    def Comb(order):
        for i in range(2, len(order) + 1):  # 조합에 들어가는 원소의 개수
            for j in range(0, len(order)):
                string = ""

                CalcComb(string, order, j, 0, i)

    def CalcComb(string, order, index, depth, length):
        string = string + order[index]
        depth = depth + 1

        if (depth == length):
            if string in orderComb.keys():
                orderComb[string] += 1

            else:
                orderComb[string] = 1

            return string

        for i in range(index + 1, len(order)):
            CalcComb(string, order, i, depth, length)

    global orderComb
    orderComb = {}

    answer = []

    for order in orders:
        temp = []

        for i in range(len(order)):  # order를 오름차순으로 정렬
            temp.append(order[i])
        temp.sort()
        order = "".join(temp)

        Comb(order)

    tempDict = {}
    for key in orderComb:
        if (orderComb[key] >= 2):
            tempDict[key] = orderComb[key]

    orderComb = tempDict
    for c in course:
        temp = []
        maxCount = 0

        for key in orderComb.keys():
            if (len(key) == c):
                if (orderComb[key] > maxCount):
                    maxCount = orderComb[key]
                    temp.clear()
                    temp.append(key)

                elif (orderComb[key] == maxCount):
                    temp.append(key)

        answer = answer + temp
    answer.sort()

    return answer
