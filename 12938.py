def solution(n, s):
    answer = []

    if (s < n):  # 존재 불가
        return [-1]

    for i in range(n, 0, -1):
        q = s // i

        answer.append(q)

        s -= q

    answer.sort()

    return answer
