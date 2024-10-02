def solution(A, B):
    point = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    nod = 0
    for a in A:
        while (nod < len(B)):
            if (B[nod] <= a):
                break

            else:
                nod += 1

        if (nod == 0):  # a보다 더 큰 숫자가 없다면
            B.pop()  # 가장 작은 숫자 제거
            nod = 0

        else:
            nod -= 1
            B.pop(nod)
            point += 1

    return point
