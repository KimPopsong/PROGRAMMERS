from collections import Counter
import copy


def solution(topping):
    answer = 0

    list1 = topping[0:1]
    list2 = topping[1:len(topping)]

    list1 = Counter(list1)
    list2 = Counter(list2)

    if (len(list1) == len(list2)):
        answer = answer + 1

    for i in range(1, len(topping)):
        list1[topping[i]] = list1[topping[i]] + 1
        list2[topping[i]] = list2[topping[i]] - 1

        if (list2[topping[i]] == 0):
            list2.pop(topping[i])

        if (len(list1) == len(list2)):
            answer = answer + 1

    return answer
