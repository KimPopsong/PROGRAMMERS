def solution(genres, plays):
    answer = []

    genreRank = dict()  # 많이 재생된 장르 최대 힙
    genrePlay = dict()

    for i in range(len(genres)):
        if (genres[i] in genreRank.keys()):
            genreRank[genres[i]] += plays[i]
            genrePlay[genres[i]].append([plays[i], i])

        else:
            genreRank[genres[i]] = plays[i]
            genrePlay[genres[i]] = []
            genrePlay[genres[i]].append([plays[i], i])

    genreRank = [[v, k] for k, v in genreRank.items()]
    genreRank.sort(reverse=True)

    for genre in genreRank:
        genre = genre[1]

        play = sorted(genrePlay[genre], key=lambda x: x[1])  # 장르 내에서 재생 횟수가 같을 경우 고유 번호가 낮은 노래 먼저 수록
        play = sorted(play, reverse=True, key=lambda x: x[0])  # 장르 내에서 많이 재생된 노래 먼저 수록

        for i, p in enumerate(play):
            if (i >= 2):
                break

            answer.append(p[1])

    return answer
