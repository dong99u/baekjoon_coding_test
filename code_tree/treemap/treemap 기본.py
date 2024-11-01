from sortedcontainers import SortedDict
import sys

input = sys.stdin.readline

sd = SortedDict()

n = int(input())

for _ in range(n):
    input_list = input().rstrip().split()

    if input_list[0] == 'add':
        sd[input_list[1]] = input_list[2]

    elif input_list[0] == 'remove':
        sd.pop(input_list[1])

    elif input_list[0] == 'find':
        if input_list[1] in sd:
            print(sd[input_list[1]])
        else:
            print(None)

    elif input_list[0] == 'print_list':
        for key, value in sd.items():
            print(value, end=' ')




