from itertools import permutations
import re


def solution(userId, bannedId):
    answer = []

    bannedId = [i.replace("*", ".") for i in bannedId]

    for comb in permutations(userId, len(bannedId)):
        comb = list(comb)

        flag = True
        for i in range(len(bannedId)):
            if (re.match(bannedId[i], comb[i]) and len(bannedId[i]) == len(comb[i])):
                continue

            else:
                flag = False
                break

        if (flag):
            answer.append(tuple(sorted(comb)))

    answer = set(answer)

    return len(answer)
