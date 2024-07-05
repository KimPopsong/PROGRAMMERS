from collections import deque


def solution(plans):
    answer = []

    plans = sorted(plans, key=lambda x: x[1])  # 과제 시작 순으로 정렬
    leftPlans = deque()  # 잔여 과제를 stack으로 관리

    i = 0
    for i in range(len(plans) - 1):  # 가용시간 내 끝낼 수 있는 과제부터 계산
        frontHour, frontMinute = plans[i][1].split(":")
        rearHour, rearMinute = plans[i + 1][1].split(":")

        availTime = (int(rearHour) - int(frontHour)) * 60 + (int(rearMinute) - int(frontMinute))  # 문제를 풀 수 있는 가용시간

        if (availTime >= int(plans[i][2])):  # 가용시간이 playtime보다 작다면 문제를 다 풂
            answer.append(plans[i][0])

            availTime = availTime - int(plans[i][2])
            while (availTime and len(leftPlans)):  # 문제를 다 풀고 남는 시간이 있다면 미뤄둔 과제 풀기
                if (availTime >= leftPlans[-1][2]):
                    availTime -= leftPlans[-1][2]
                    answer.append(leftPlans[-1][0])
                    leftPlans.pop()
                    print(leftPlans)

                else:
                    leftPlans[-1][2] = leftPlans[-1][2] - availTime
                    break


        else:  # 가용시간이 부족하면 playtime에서 가용시간을 빼고 stack에 추가
            plans[i][2] = int(plans[i][2]) - availTime
            leftPlans.append(plans[i])

    answer.append(plans[-1][0])  # 마지막 과제는 항상 끝나므로 추가

    while len(leftPlans):  # 잔여 과제가 있다면 처리
        answer.append(leftPlans.pop()[0])

    return answer
