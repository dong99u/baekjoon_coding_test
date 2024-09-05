from collections import deque

k = int(input())

stack = deque()

current_number = 1

answers = []

for i in range(k):
    n = int(input())
    while current_number <= n:
        stack.append(current_number)
        answers.append("+")
        current_number += 1
    if stack[-1] == n:
        stack.pop()
        answers.append("-")
    else:
        print("NO")
        exit()

for answer in answers:
    print(answer)

