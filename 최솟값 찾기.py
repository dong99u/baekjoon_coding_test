from collections import deque

N, L = map(int, input().split())

num_list = list(map(int, input().split()))

dq = deque()

for i in range(N):
    while dq and dq[-1][0] > num_list[i]:
        dq.pop()

    dq.append((num_list[i], i))
    if dq[0][1] <= i - L:
        dq.popleft()

    print(dq[0][0], end=' ')




