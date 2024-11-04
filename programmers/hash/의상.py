from collections import defaultdict


def solution(clothes):

    answer = 1

    d = defaultdict(int)

    for cloth, type in clothes:
        d[type] += 1

    for type in d:
        answer *= d[type] + 1

    return answer - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
            ["crow_mask", "face"],
            ["smoky_makeup", "face"],
        ]
    )
)
