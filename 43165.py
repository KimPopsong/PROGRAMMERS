def solution(numbers, target):
    global answer

    answer = 0
    number = []

    def calc():
        global answer

        if (sum(number) == target):
            answer = answer + 1

    def recursion(depth):
        if (depth == len(numbers)):
            calc()

            return

        number.append(numbers[depth])
        recursion(depth + 1)
        number.pop()

        number.append(numbers[depth] * -1)
        recursion(depth + 1)
        number.pop()

        return

    recursion(0)

    return answer
