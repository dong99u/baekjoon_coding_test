from collections import deque


def solution(s):
    q = deque()

    for elem in s:
        if elem == "(":
            q.append(elem)
        else:
            if len(q) == 0 or q[-1] == ")":
                return False
            else:
                q.pop()

    if len(q) != 0:
        return False
    return True


print(solution(")()()"))
