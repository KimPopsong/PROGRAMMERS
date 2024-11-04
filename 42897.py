def solution(money):
    answer = 0

    if (len(money) == 3):  # 집이 3채라면 한 채 밖에 고르지 못함
        return max(money)

    money1 = money[0:len(money) - 1]  # 첫 번째 집을 무조건 선택
    money2 = money[1:len(money)]  # 두 번째 집을 무조건 선택

    dp1 = [money[0], money[1], money[0] + money[2]]
    dp2 = [money[1], money[2], money[1] + money[3]]

    for i in range(3, len(money) - 1):
        if (dp1[i - 2] > dp1[i - 3]):
            dp1.append(dp1[i - 2] + money1[i])

        else:
            dp1.append(dp1[i - 3] + money1[i])

        if (dp2[i - 2] > dp2[i - 3]):
            dp2.append(dp2[i - 2] + money2[i])

        else:
            dp2.append(dp2[i - 3] + money2[i])

    answer = max(max(dp1), max(dp2))

    return answer
