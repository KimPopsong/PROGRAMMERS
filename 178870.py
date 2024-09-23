def solution(sequence, k):
    answer = [0, len(sequence) - 1]

    length = len(sequence)
    head = 0
    tail = 0
    sumTemp = sequence[0]

    while (True):
        if (sumTemp == k):  # 합이 k와 같다면
            if (head - tail + 1 < answer[1] - answer[0] + 1):  # 부분 수열의 개수 확인 후, 개수가 적을시 교체
                answer[0] = tail
                answer[1] = head

            sumTemp = sumTemp - sequence[tail]  # tail 이동
            tail = tail + 1

        elif (sumTemp < k):  # 합이 k보다 작을시 head 이동
            head = head + 1

            if (head >= length):  # head가 수열의 길이를 넘어가면 반복문 탈출
                break

            else:  # sumTemp에 head 더하기
                sumTemp = sumTemp + sequence[head]

        else:  # 합이 k보다 클시 tail 이동
            if (tail == head):  # head와 tail이 같은데 k보다 크다면, 뒤에 값들은 k보다 무조건 크기때문에 탈출
                break

            else:
                sumTemp = sumTemp - sequence[tail]  # sumTemp에 tail 빼기
                tail = tail + 1

    return answer
