from collections import deque


def solution(order):
    package = 0  # 트럭에 실린 택배의 개수

    belt = deque()
    subBelt = []

    for i in range(1, len(order) + 1):
        belt.append(i)

    nod = 0
    while (nod < len(order)):
        if (len(belt) == 0):  # 벨트가 비었다면
            top = 1000001

        else:
            top = belt[0]

        if (top < order[nod]):
            subBelt.append(top)
            belt.popleft()

        elif (top > order[nod]):
            if (len(subBelt) == 0):
                break

            subTop = subBelt.pop()

            if (subTop == order[nod]):
                nod = nod + 1
                package = package + 1

            else:
                break

        else:
            belt.popleft()
            nod = nod + 1
            package = package + 1

    return package
