from collections import deque


def solution(arr):
    stack = deque()

    answer = []
    for i, num in enumerate(arr):
        if i == 0:
            stack.append(num)
            continue
        if stack[-1] != num:
            answer.append(stack.pop())
        stack.append(num)

    answer.append(stack.pop())

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
