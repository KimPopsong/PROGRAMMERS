def solution(picks, minerals):
    fatigue = 0  # 피로도

    mineralWeight = []  # 5덩이로 묶어서 가중치 구하기
    pick = []  # 곡괭이 사용 순서

    count = 0
    weight = 0
    for i in range(len(minerals)):
        if (minerals[i] == "diamond"):
            weight = weight + 25

        elif (minerals[i] == "iron"):
            weight = weight + 5

        else:
            weight = weight + 1

        count = count + 1

        if (count == 5):
            mineralWeight.append([i // 5, weight])
            count = 0
            weight = 0
    if (count != 5):
        mineralWeight.append([len(minerals) // 5, weight])

    for i in range(len(mineralWeight) - 1, -1, -1):
        if (mineralWeight[i][0] >= sum(picks)):  # 광물이 곡괭이의 수보다 많다면
            mineralWeight.remove(mineralWeight[i])  # 뒤의 광물 제거

        else:
            break

    mineralWeight = sorted(mineralWeight, key=lambda x: x[1], reverse=True)  # 가중치로 내림차순 정렬
    for m in mineralWeight:  # 가중치 순으로
        for i in range(len(picks)):
            if (picks[i] != 0):
                if (i == 0):  # 다이아몬드 곡괭이
                    m.append("diamond")

                elif (i == 1):  # 철 곡괭이
                    m.append("iron")

                else:  # 돌 곡괭이
                    m.append("stone")

                picks[i] = picks[i] - 1
                break

    mineralWeight = sorted(mineralWeight, key=lambda x: x[0])  # 가중치로 내림차순 정렬
    for m in mineralWeight:  # 가중치 순으로
        if (m[2] == "diamond"):
            pick.append("diamond")

        elif (m[2] == "iron"):
            pick.append("iron")

        else:
            pick.append("stone")

    for i in range(len(minerals)):
        if (i >= len(pick) * 5):
            break

        pickage = pick[i // 5]
        if (minerals[i] == "diamond" and pickage == "iron"):
            fatigue = fatigue + 5

        elif (minerals[i] == "diamond" and pickage == "stone"):
            fatigue = fatigue + 25

        elif (minerals[i] == "iron" and pickage == "stone"):
            fatigue = fatigue + 5

        else:
            fatigue = fatigue + 1

    return fatigue
