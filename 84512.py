def solution(word):
    global alphabets, maxLength, dictionary

    def makeDict(string, length):
        if (length == maxLength):
            dictionary.append(string)  # 사전에 추가

            return 0

        for alpha in alphabets:
            makeDict(string + alpha, length + 1)

        return 0

    answer = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for length in range(1, 6):  # 단어의 길이
        maxLength = length

        for alpha in alphabets:
            makeDict(alpha, 1)

    dictionary.sort()

    answer = dictionary.index(word) + 1

    return answer
