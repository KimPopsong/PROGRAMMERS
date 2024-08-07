import math


def getGCD(i, j):
    if (i < j):
        i, j = j, i

    gcd = 1

    while (gcd):
        gcd = i % j
        i = j
        j = gcd

    return i


def solution(w, h):
    gcd = getGCD(w, h)

    square = ((w // gcd) + (h // gcd) - 1) * gcd

    return w * h - square
