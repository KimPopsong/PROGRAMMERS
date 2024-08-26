def solution(array, commands):
    answer = []

    for command in commands:
        slicedString = array[command[0] - 1:command[1]]
        slicedString.sort()
        answer.append(slicedString[command[2] - 1])

    return answer
