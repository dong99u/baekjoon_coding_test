def solution(s: str):

    result = []
    t = []
    s = s[2:-2].split("},{")
    for i, w in enumerate(s):
        w = w.split(",")
        w = list(map(int, w))
        result.append(w)

    result.sort(key=len)

    answer = {}
    for i in result:
        for j in i:
            if j not in answer:
                answer[j] = 1
    return list(answer.keys())


s = input()
print(solution(s))
