def solution(sizes):
    maxWidth = 0
    maxHeight = 0

    for card in sizes:
        w, h = card

        if (w > h):  # 항상 h가 크도록
            w, h = h, w

        if (maxWidth < w):
            maxWidth = w

        if (maxHeight < h):
            maxHeight = h

    return maxWidth * maxHeight
