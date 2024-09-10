from collections import deque

s = input()

stack = deque()

result = 0
for num in s:
    num = int(num)

    stack.append(num)

    if len(stack) == 2:
        a = stack.pop()
        b = stack.pop()

        if a == 0 or b == 0:
            result += a + b
        else:
            result = a * b

        stack.append(result)

print(result)