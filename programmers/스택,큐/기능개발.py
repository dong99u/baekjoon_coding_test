from collections import deque
import math


def solution(progresses, speeds):

    days = deque()

    n = len(progresses)

    for i in range(n):
        left_days = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(left_days)

    answer = []

    prev = days.popleft()
    count = 1
    for i in range(1, n):
        curr = days.popleft()
        if curr <= prev:
            count += 1
        else:
            prev = curr
            answer.append(count)
            count = 1

    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
