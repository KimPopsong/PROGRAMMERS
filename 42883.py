def solution(number, k):
    answer = ""
    stack = []

    nod = 0
    while (nod < len(number)):
        while (len(stack) and stack[-1] < number[nod] and k > 0):
            stack.pop()
            k = k - 1

        stack.append(number[nod])
        nod = nod + 1

    for i in range(len(stack) - k):
        answer = answer + stack[i]

    return answer
