def solution(s):
    correct = 0
    string = list(s)

    for i in range(len(s)):
        stack = []
        flag = True

        for st in string:
            if (st == "[" or st == "{" or st == "("):
                stack.append(st)
                flag = False

            elif (len(stack)):
                if (stack[-1] == "[" and st == "]"):
                    stack.pop()

                elif (stack[-1] == "{" and st == "}"):
                    stack.pop()

                elif (stack[-1] == "(" and st == ")"):
                    stack.pop()

        if (len(stack) == 0 and flag == False):
            correct = correct + 1

        string.append(string[0])
        del string[0]

    return correct
