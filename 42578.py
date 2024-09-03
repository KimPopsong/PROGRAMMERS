def solution(clothes):
    answer = 1

    clothesDict = dict()

    for cloth in clothes:
        if cloth[1] in clothesDict.keys():
            clothesDict[cloth[1]] += 1

        else:
            clothesDict[cloth[1]] = 1

    for val in clothesDict.values():
        temp = val + 1

        answer *= temp
    answer -= 1

    return answer
