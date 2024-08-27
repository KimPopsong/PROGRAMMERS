def solution(s):
    string = sorted(map(int, s.split()), reverse=True)

    answer = str(string[-1]) + ' ' + str(string[0])

    return answer
