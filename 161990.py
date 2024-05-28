def solution(wallpaper):
    answer = []

    row = len(wallpaper)
    col = len(wallpaper[0])

    top = 100
    bottom = 0
    left = 100
    right = 0

    for i in range(row):
        for j in range(col):
            if (wallpaper[i][j] == '#'):
                if (top > i):
                    top = i

                if (bottom < i + 1):
                    bottom = i + 1

                if (left > j):
                    left = j

                if (right < j + 1):
                    right = j + 1

    answer.append(top)
    answer.append(left)
    answer.append(bottom)
    answer.append(right)

    return answer
