def solution(n):
    binCount = str(bin(n)).count("1")  # n을 이진수로 변환했을 때 1의 갯수

    x = n + 1
    while (True):
        if (str(bin(x)).count("1") == binCount):
            break

        else:
            x = x + 1
            
    return x
