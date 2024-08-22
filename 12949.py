def solution(arr1, arr2):
    answer = []

    m = len(arr1)  # arr1의 행
    n = len(arr2)  # arr1의 열, arr2의 행
    r = len(arr2[0])  # arr2의 열

    for i in range(m):
        temp = []

        for j in range(r):
            sumTemp = 0

            for k in range(n):
                sumTemp = sumTemp + arr1[i][k] * arr2[k][j]

            temp.append(sumTemp)

        answer.append(temp)

    return answer
