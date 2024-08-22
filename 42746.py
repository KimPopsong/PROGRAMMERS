def solution(numbers):
    if (sum(numbers) == 0):
        return "0"

    answer = ""

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    for num in numbers:
        answer = answer + str(num)

    return answer
