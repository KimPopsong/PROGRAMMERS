def solution(record):
    answer = []

    userNicknameDict = dict()

    for rec in record:  # userId에 따른 nickname 최신화
        message = rec.split()

        if (message[0] == "Enter" or message[0] == "Change"):
            userNicknameDict[message[1]] = message[2]

    for rec in record:
        message = rec.split()

        if (message[0] == "Enter"):
            answer.append(userNicknameDict[message[1]] + "님이 들어왔습니다.")

        elif (message[0] == "Leave"):
            answer.append(userNicknameDict[message[1]] + "님이 나갔습니다.")

        else:
            continue

    return answer
