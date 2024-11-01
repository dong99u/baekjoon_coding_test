from collections import defaultdict


def solution(participant: list, completion: list):
    answer = ""

    d = defaultdict(int)

    for p in participant:
        d[p] += 1

    for c in completion:
        if c in d:
            d[c] -= 1

        if d[c] == 0:
            del d[c]

    return list(d.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
