def solution(n):
    answer = []

    snail = []
    for i in range(n):
        temp = [0 for i in range(i + 1)]
        snail.append(temp)

    nod = 1
    r = 0
    c = 0
    dr = [1, 0, -1]  # 좌표의 움직임은 [아래, 오른쪽, 위] 순
    dc = [0, 1, -1]  # 위로 올라갈때는 r과 c의 좌표가 1씩 감소해야함
    delta = 0
    while (nod <= sum(range(1, n + 1))):
        snail[r][c] = nod

        if (not (0 <= r + dr[delta] < n) or not (0 <= c + dc[delta] < n) or (
                snail[r + dr[delta]][c + dc[delta]] != 0)):  # 배열의 범위를 벗어나거나, 기존에 값이 있다면 방향 전환
            delta = delta + 1

            if (delta > 2):
                delta = 0

        r = r + dr[delta]
        c = c + dc[delta]

        nod = nod + 1

    for l in snail:
        for n in l:
            answer.append(n)

    return answer
