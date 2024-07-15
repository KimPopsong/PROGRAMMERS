from collections import Counter


def solution(weights):
    partner = 0

    weights = Counter(weights)

    for w in weights:
        partner = partner + weights[w] * (weights[w] - 1) / 2  # Combination. 같은 원소가 여러 개일 때
        partner = partner + weights[w] * weights[w * 2 / 4]
        partner = partner + weights[w] * weights[w * 2 / 3]
        partner = partner + weights[w] * weights[w * 4 / 3]

    return partner
