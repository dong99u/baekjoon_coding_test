from collections import defaultdict


def solution(genres, plays):

    genre_total_play = defaultdict(int)

    genre_songs = defaultdict(list)

    for i in range(len(genres)):
        genre_total_play[genres[i]] += plays[i]
        genre_songs[genres[i]].append((plays[i], i))

    sorted_genres = sorted(
        genre_total_play.keys(), key=lambda x: genre_total_play[x], reverse=True
    )

    answer = []
    # 2. 각 장르별로 노래 선택
    for genre in sorted_genres:
        # 장르 내 노래를 재생 횟수(내림차순)와 고유번호(오름차순)로 정렬
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))

        # 장르별로 최대 2곡 선택
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][1])

    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
