from collections import defaultdict

def initialize_info(info):
    dict = defaultdict(int)

    dict['A'] = info[0]
    dict['C'] = info[1]
    dict['G'] = info[2]
    dict['T'] = info[3]

    return dict

def check(temp, info):
    for key in info.keys():
        if temp[key] < info[key]:
            return False

    return True


def initialize():
    s, p = map(int, input().split())

    dna = input()

    info = list(map(int, input().split()))
    info = initialize_info(info)

    return s, p, dna, info

def solution():
    s, p, dna, info = initialize()
    answer = 0

    left = 0
    right = left + p - 1

    temp = defaultdict(int)

    for i in range(left, right + 1):
        temp[dna[i]] += 1

    while right < s:
        if check(temp, info):
            answer += 1

        temp[dna[left]] -= 1
        left += 1

        right += 1
        if right >= s:
            break
        temp[dna[right]] += 1

    return answer


print(solution())


