import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))

heap = []

for num in arr:
    heapq.heappush(heap, num)

    if len(heap) < 3:
        print(-1)
        continue


