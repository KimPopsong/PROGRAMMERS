def solution(s):
    answer = ''

    s = s.lower()

    flag = True
    for i in range(len(s)):
        if (flag and s[i] != " "):
            if ('0' <= s[i] <= '9'):
                answer = answer + s[i]

            else:
                answer = answer + s[i].upper()

            flag = False

        else:
            if (s[i] == " "):
                answer = answer + s[i]
                flag = True

            else:
                answer = answer + s[i]

    return answer
