import copy


def solution(elements):
    numSet = set()

    for i in range(0, len(elements)):  # 연속 부분 수열의 원소의 개수
        tempElements = copy.deepcopy(elements)

        for j in range(0, i):
            tempElements.append(elements[j])

        for j in range(0, len(elements)):
            numSet.add(sum(tempElements[j:j + i + 1]))

    return len(numSet)
