def solution(numbers):
    answer = []

    for number in numbers:
        s = str(bin(number))  # 2진수로 변환
        s = s[2:]  # 이진수 표기 제거(0b)

        flag = True
        nod = 1
        for i in range(len(s) - 1, -1, -1):  # 뒤에서부터 0 탐색
            if (s[i] == "0"):
                break

            else:
                nod = nod * 2

        temp = number | nod
        temp = temp ^ (nod // 2)

        answer.append(temp)

    return answer
