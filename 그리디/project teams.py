import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

result = float('inf')
for start in range(2 * n):
    end = 2 * n - start - 1

    result = min(result, num_list[start] + num_list[end])

print(result)