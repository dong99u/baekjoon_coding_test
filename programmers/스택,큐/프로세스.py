from collections import deque


def solution(priorities, location):
    q = deque()
    for i, priority in enumerate(priorities):
        q.append((priority, i))

    result = []
    while q:

        head_priority, head_idx = q.popleft()

        is_priority = True
        for priority, idx in q:
            if priority > head_priority:
                is_priority = False
                break

        if is_priority == False:
            q.append((head_priority, head_idx))
        else:
            result.append((head_priority, head_idx))

    answer = -1

    for idx, (p, i) in enumerate(result):
        if i == location:
            answer = idx + 1

    return answer


print(solution([2, 1, 3, 2], 2))
