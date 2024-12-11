def solution(videoLength, pos, opStart, opEnd, commands):
    videoLengthToSec = int(videoLength.split(":")[0]) * 60 + int(videoLength.split(":")[1])  # 비디오의 전체 재생 시간을 초로 환산
    posToSec = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])  # 현재 재생 시간을 초로 환산
    opStartToSec = int(opStart.split(":")[0]) * 60 + int(opStart.split(":")[1])
    opEndToSec = int(opEnd.split(":")[0]) * 60 + int(opEnd.split(":")[1])
    
    if (opStartToSec <= posToSec <= opEndToSec):  # 오프닝 건너뛰기
            posToSec = opEndToSec
    
    for command in commands:
        if (command == "prev"):  # 10초 앞으로
            posToSec -= 10
            
            if (posToSec < 0):
                posToSec = 0
                
        elif (command == "next"):  # 10초 뒤로
            posToSec += 10
            
            if (posToSec >= videoLengthToSec):
                posToSec = videoLengthToSec
                
        if (opStartToSec <= posToSec <= opEndToSec):  # 오프닝 건너뛰기
            posToSec = opEndToSec
    
    pos = ""
    
    if (posToSec // 60 < 10):  # 결과가 한자리 수라면
        pos += "0" + str(posToSec // 60)
        
    else:
        pos += str(posToSec // 60)
    pos += ":"    
    
    if (posToSec % 60 < 10):  # 결과가 한자리 수라면
        pos += "0" + str(posToSec % 60)
        
    else:
        pos += str(posToSec % 60)
        
    return pos
