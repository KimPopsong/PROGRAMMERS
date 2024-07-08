def solution(book_time):
    book_time = sorted(book_time, key=lambda x: x[0])  # 시작시간 기준으로 오름차순 정렬

    for i in range(len(book_time)):  # 분으로 환산
        startHour, startMinute = map(int, book_time[i][0].split(":"))
        endHour, endMinute = map(int, book_time[i][1].split(":"))
        book_time[i] = [startHour * 60 + startMinute, endHour * 60 + endMinute]

    room = []
    maxRoom = 0

    for i in range(len(book_time)):
        for j in room:
            if (j <= book_time[i][0]):  # 기존에 있던 방 사용이 끝났다면
                room.remove(j)  # 방 삭제

        room.append(book_time[i][1] + 10)  # 청소시간 10분 고려, 사용종료 + 청소시간을 배열에 추가

        if (len(room) > maxRoom):
            maxRoom = len(room)

    return maxRoom
