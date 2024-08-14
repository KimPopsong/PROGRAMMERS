def solution(s):
    stack = []

    for string in s:
        if string == "(":
            stack.append("(")

        else:
            if len(stack) == 0:
                return False

            elif stack[-1] == "(":
                stack.pop()

            else:
                continue

    if len(stack):
        return False

    return True
