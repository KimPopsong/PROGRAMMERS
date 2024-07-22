def solution(cards):
    groups = []

    while (True):
        index = -1
        for i in range(len(cards)):
            if (cards[i] != 0):
                index = i
                break

        if (index == -1):
            break

        temp = []
        while (True):
            if (cards[index] == 0):
                break

            tempIndex = cards[index]
            temp.append(cards[index])
            cards[index] = 0
            index = tempIndex - 1
        groups.append(temp)

    groups = sorted(groups, key=lambda x: len(x), reverse=True)  # 개수 순으로 내림차순 정렬

    if (len(groups) == 1):  # 그룹이 한 개일 경우
        return 0

    else:  # 두 개 이상일 경우
        return len(groups[0]) * len(groups[1])
