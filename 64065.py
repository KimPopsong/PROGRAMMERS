def solution(s):
    answer = []

    string = []

    s = s.split("},{")
    for ss in s:
        ss = ss.replace("{", "")
        ss = ss.replace("}", "")
        string.append(list(map(int, ss.split(","))))
    string.sort(key=lambda x: len(x))

    for st in string:
        for s in st:
            if s in answer:
                continue

            else:
                answer.append(s)
                
    return answer
