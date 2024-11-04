from collections import defaultdict


def solution(genres, plays):
    plays_sum = defaultdict(int)
    g = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        g[genre].append((play, i))
        plays_sum[genre] += play

    for key in g:
        g[key].sort(key=lambda x: (-x[0], x[1]))

    sorted_plays_sum = sorted(
        plays_sum.keys(), key=lambda x: plays_sum[x], reverse=True
    )

    answer = []

    for genre in sorted_plays_sum:
        for i in range(min(len(g[genre]), 2)):
            answer.append(g[genre][i][1])

    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
