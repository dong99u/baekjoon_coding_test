import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
input_list = list(map(int, input().split()))

if n < k:
    print(0)
    exit()

input_list.sort()

diffs = []
for i in range(n - 1):
    diff = input_list[i + 1] - input_list[i]

    diffs.append(diff)


diffs.sort(reverse=True)

for i in range(k - 1):
    diffs.pop(0)

print(sum(diffs))