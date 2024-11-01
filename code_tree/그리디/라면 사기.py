import sys

input = sys.stdin.readline

n = int(input())
factories = list(map(int, input().split()))

answer = 0
i = 0

while i < n:
    # Case where we can buy from i, i+1, and i+2
    if i + 2 < n and factories[i + 1] > factories[i + 2]:
        min_purchase = min(factories[i], factories[i + 1] - factories[i + 2])
        answer += 5 * min_purchase
        factories[i] -= min_purchase
        factories[i + 1] -= min_purchase

    # Case where we can buy from i, i+1, and i+2 (regular 3-factory buy)
    if i + 2 < n and factories[i] > 0 and factories[i + 1] > 0 and factories[i + 2] > 0:
        min_purchase = min(factories[i], factories[i + 1], factories[i + 2])
        answer += 7 * min_purchase
        factories[i] -= min_purchase
        factories[i + 1] -= min_purchase
        factories[i + 2] -= min_purchase

    # Case where we can buy from i and i+1
    if i + 1 < n and factories[i] > 0 and factories[i + 1] > 0:
        min_purchase = min(factories[i], factories[i + 1])
        answer += 5 * min_purchase
        factories[i] -= min_purchase
        factories[i + 1] -= min_purchase

    # Case where we only buy from i
    if factories[i] > 0:
        answer += 3 * factories[i]
        factories[i] = 0

    i += 1

print(answer)
