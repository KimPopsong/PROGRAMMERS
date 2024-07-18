def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: x[0], reverse=True)  # 첫 번째 값으로 내림차순 정렬을 한 뒤
    data = sorted(data, key=lambda x: x[col - 1])  # col의 값으로 오름차순 정렬

    dataS = []

    for i in range(len(data)):
        temp = 0

        for d in data[i]:
            temp = temp + (d % (i + 1))
        dataS.append(temp)

    answer = 0
    for i in range(row_begin - 1, row_end):
        answer = answer ^ dataS[i]

    return answer
