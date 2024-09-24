def solution(scaleRemember, musicinfos):
    def changeScale(music):  # #이 붙은 문자를 치환
        music = music.replace("C#", "H")
        music = music.replace("D#", "I")
        music = music.replace("F#", "J")
        music = music.replace("G#", "K")
        music = music.replace("A#", "L")
        music = music.replace("B#", "M")

        return music

    answer = ''
    playTime = 0
    scaleRemember = changeScale(scaleRemember)

    for info in musicinfos:
        startTime, endTime, musicName, scales = info.split(",")

        startTime = list(map(int, startTime.split(":")))
        endTime = list(map(int, endTime.split(":")))

        time = (endTime[0] - startTime[0]) * 60 + (endTime[1] - startTime[1])  # 분으로 환산

        playedScales = ""

        scales = changeScale(scales)

        nod = 0
        for i in range(time):
            playedScales = playedScales + scales[nod]

            nod = nod + 1

            if (nod >= len(scales)):
                nod = 0

        if (scaleRemember in playedScales):  # 들었던 음계가 플레이된 음계에 있다면
            if (playTime < time):  # 재생된 시간이 기존보다 길다면
                playTime = time  # 교체
                answer = musicName

    if (answer == ""):
        return "(None)"

    return answer
