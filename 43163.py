def solution(begin, target, words):
    def recursion(word, index):
        global answer

        isVisit[index] = True

        if (word == target):  # target으로 변환이 완료되었다면
            if (answer == 0):  # 변환된 적이 없다면
                answer = isVisit.count(True)

            else:  # 변환된 적이 있다면
                answer = min(isVisit.count(True) - 1, answer)  # 최솟값 삽입

        else:
            for i in range(len(words)):
                if (isVisit[i] == False):  # 방문한 적이 없는 단어면
                    diff = 0
                    for j in range(len(begin)):  # 스펠링 비교
                        if (word[j] != words[i][j]):
                            diff += 1

                    if (diff == 1):  # 스펠링이 한 개 차이라면
                        recursion(words[i], i)

        isVisit[index] = False

    global answer
    answer = 0

    global isVisit
    isVisit = [False for i in range(len(words))]

    for i in range(len(words)):
        recursion(begin, i)

    return answer
