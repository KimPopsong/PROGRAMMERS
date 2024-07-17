from collections import Counter


def solution(k, tangerine):
    diffSize = 0

    tangerine = Counter(tangerine)

    dict = tangerine.most_common()

    for d in dict:
        diffSize = diffSize + 1

        k = k - d[1]

        if (k <= 0):
            break

    return diffSize
