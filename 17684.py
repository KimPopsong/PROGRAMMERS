def solution(msg):
    answer = []

    dictionary = dict()
    index = 27

    for c in range(1, 27):  # 'A' ~ 'Z' 사전에 넣기
        dictionary[chr(c + 64)] = c

    nod = 0
    while (nod <= len(msg) - 1):
        nod2 = 1
        temp = msg[nod]
        while (nod + nod2 <= len(msg)):
            temp = msg[nod:nod + nod2]

            if (temp in dictionary.keys()):
                nod2 = nod2 + 1

            else:
                break

        if (temp in dictionary.keys()):
            answer.append(dictionary[temp])

            break

        else:
            dictionary[temp] = index
            index = index + 1

        nod = nod + nod2 - 1
        answer.append(dictionary[temp[0:nod2 - 1]])

    return answer
