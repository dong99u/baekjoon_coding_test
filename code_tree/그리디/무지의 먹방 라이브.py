import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for idx, elem in enumerate(food_times):
        heapq.heappush(q, (elem, idx + 1))

    sum_value = 0
    prev = 0
    length = len(food_times)

    while sum_value + (q[0][0] - prev)





print(solution([3, 1, 2], 5)) # 1