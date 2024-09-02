def solution(n, words):
    word = dict()

    turn = 0

    lastWord = words[0][0]

    while (turn < len(words)):
        w = words[turn]

        if (w in word.keys()):  # 이미 말했다면
            break

        elif (lastWord != w[0]):  # 끝말잇기가 아니라면
            break

        else:
            word[w] = 1
            lastWord = w[-1]
            turn = turn + 1

    if (len(words) == turn):
        return [0, 0]

    else:
        return [(turn % n) + 1, turn // n + 1]
