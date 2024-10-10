def solution(gems):
    def addGem(dictionary, index):
        gem = gems[index]

        if (gem in dictionary.keys()):  # 이미 있다면
            dictionary[gem] += 1

        else:
            dictionary[gem] = 1

    def subGem(dictionary, index):
        gem = gems[index]

        dictionary[gem] -= 1

        if (dictionary[gem] <= 0):
            del dictionary[gem]

    gemTypeLength = len(set(gems))  # 보석 종류의 길이

    start = 0  # 시작 지점의 index
    end = 0  # 끝 지점의 index
    haveDict = dict()  # start ~ end까지의 보석의 종류 및 개수 저장

    for index, gem in enumerate(gems):  # end값 계산
        addGem(haveDict, index)

        if ((gemTypeLength - len(haveDict)) == 0):
            end = index
            break

    answer = [1, end + 1]  # answer의 index는 1부터 시작
    length = end - start + 1  # 조건을 만족할 때, 보석의 개수 저장(최솟값으로)

    while (True):
        if ((gemTypeLength - len(haveDict)) == 0):  # 조건을 만족할 때
            if (end - start + 1 < length):  # 기존 길이보다 작다면, 값 갱신
                length = end - start + 1
                answer = [start + 1, end + 1]

            subGem(haveDict, start)  # start의 위치에 있는 보석을 제외하고
            start += 1  # start 증가

            if (start > end):
                break

        else:
            end += 1

            if (end >= len(gems)):
                break

            addGem(haveDict, end)

    return answer
