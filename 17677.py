from collections import Counter
import math


def solution(str1, str2):
    answer = 0

    str1 = str1.upper()  # 대문자로 치환
    str2 = str2.upper()  # 대문자로 치환

    s1 = []
    s2 = []

    for i in range(len(str1) - 1):  # 다중집합 만들기
        temp = ""

        if (65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90):
            temp += str1[i]
            temp += str1[i + 1]

        else:
            continue

        s1.append(temp)

    for i in range(len(str2) - 1):  # 다중집합 만들기
        temp = ""

        if (65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90):
            temp += str2[i]
            temp += str2[i + 1]

        else:
            continue

        s2.append(temp)

    c1 = Counter(s1)
    c2 = Counter(s2)

    intersection = c1 - (c1 - c2)  # 교집합
    union = c1 + c2 - intersection  # 합집합

    if (sum(union.values()) == 0):
        answer = 65536

    else:
        answer = math.floor(sum(intersection.values()) / sum(union.values()) * 65536)

    return answer
