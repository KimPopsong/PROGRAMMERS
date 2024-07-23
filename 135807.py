def solution(arrayA, arrayB):
    answer = 0

    gcd1 = arrayA[0]  # arrayA의 최대공약수
    gcd2 = arrayB[0]  # arrayB의 최대공약수

    for n in arrayA:  # 유클리드 호제법을 활용해 arrayA의 최대공약수 구하기
        num = n

        if (gcd1 > num):  # 항상 num이 크도록
            num, gcd1 = gcd1, num

        temp = num % gcd1
        while (temp != 0):
            num = gcd1
            gcd1 = temp
            temp = num % gcd1

    for n in arrayB:  # 유클리드 호제법을 활용해 arrayB의 최대공약수 구하기
        num = n

        if (gcd2 > num):  # 항상 num이 크도록
            num, gcd2 = gcd2, num

        temp = num % gcd2
        while (temp != 0):
            num = gcd2
            gcd2 = temp
            temp = num % gcd2

    for i in range(gcd1, 1, -1):
        flag = True

        if (gcd1 % i == 0):  # gcd1의 약수라면
            for n in arrayB:
                if (n % gcd1 == 0):  # 나누어 진다면
                    flag = False
                    break

        else:
            continue

        if (flag):
            answer = i
            break

    for i in range(gcd2, 1, -1):
        flag = True

        if (gcd2 % i == 0):  # gcd2의 약수라면
            for n in arrayA:
                if (n % gcd2 == 0):  # 나누어 진다면
                    flag = False
                    break

        else:
            continue

        if (flag):
            if (answer < i):
                answer = i
            break

    return answer
