from collections import deque
import copy


def solution(n, wires):
    wire = [[False for i in range(n)] for j in range(n)]
    minGap = 1000000

    for w in wires:
        n1, n2 = w

        wire[n1 - 1][n2 - 1] = True
        wire[n2 - 1][n1 - 1] = True

    for w in wires:
        tempWire = copy.deepcopy(wire)

        n1, n2 = w
        tempWire[n1 - 1][n2 - 1] = False  # 송전선 한 개 끊기
        tempWire[n2 - 1][n1 - 1] = False

        dfs = deque()
        dfs.append(0)
        isvisit = [False for i in range(n)]
        towerConnect = 0

        while (len(dfs)):
            tower = dfs.pop()
            isvisit[tower] = True
            towerConnect = towerConnect + 1
            
            for i in range(n):
                if (tempWire[tower][i]):
                    if (isvisit[i] == False):
                        isvisit[i] = True
                        dfs.append(i)

        minGap = min(minGap, abs(n - 2 * towerConnect))

    return minGap
