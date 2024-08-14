def solution(n):
    answer = 1

    for i in range(1, n // 2 + 1):
        temp = n
        nod = i
        
        while (temp > 0):
            temp = temp - nod
            nod = nod + 1

        if (temp == 0):
            answer = answer + 1

    return answer
