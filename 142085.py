from queue import PriorityQueue


def solution(n, k, enemy):
    clearRound = 0
    clearEnemies = PriorityQueue()

    for e in enemy:
        clearEnemies.put(e)

        if (k > 0):  # 무적권이 있다면 무적권 먼저 사용
            k = k - 1
            clearRound = clearRound + 1

        else:  # 무적권이 없다면, 가장 적은 적부터 병사 소모
            minEnemy = clearEnemies.get()

            if (minEnemy <= n):
                n = n - minEnemy
                clearRound = clearRound + 1

            else:  # 병사가 더 적다면
                break  # 클리어 불가능

    return clearRound
