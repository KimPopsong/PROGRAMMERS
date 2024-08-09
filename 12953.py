def solution(arr):
    def calcGCD(num1, num2):  # 두 수의 최대공약수 구하기
        if (num1 < num2):
            num1, num2 = num2, num1

        gcd = 1
        while (gcd > 0):
            gcd = num1 % num2
            num1 = num2
            num2 = gcd

        return num1

    answer = 1
    for i in range(len(arr) - 1):
        gcd = calcGCD(arr[i], arr[i + 1])
        lcm = arr[i] * arr[i + 1] // gcd
        arr[i + 1] = lcm

    return arr[-1]
