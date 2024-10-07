def solution(sticker):
    answer = 0

    if (len(sticker) <= 3):  # 스티커의 개수가 3개 이하라면
        return max(sticker)  # 가장 숫자가 큰 한 개밖에 뽑지 못함

    sticker1 = sticker[0:len(sticker) - 1]  # 1번 스티커를 선택하는 경우
    sticker2 = sticker[1:len(sticker)]  # 2번 스티커를 선택하는 경우

    dp1 = sticker1[0:2]
    dp1.append(sticker1[0] + sticker1[2])
    dp2 = sticker2[0:2]
    dp2.append(sticker2[0] + sticker2[2])

    for i in range(3, len(sticker) - 1):
        dp1.append(max(sticker1[i] + dp1[i - 2], sticker1[i] + dp1[i - 3]))

    for i in range(3, len(sticker) - 1):
        dp2.append(max(sticker2[i] + dp2[i - 2], sticker2[i] + dp2[i - 3]))
    
    answer = max(max(dp1), max(dp2))

    return answer
