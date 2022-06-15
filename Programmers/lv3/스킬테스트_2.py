def solution(genres, plays):
    answer = []
    from collections import defaultdict
    """
    - 스트리밍 사이트에서 장르별로 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시하려 한다.
    1. 속한 노래가 많이 재생된 장르를 먼저 수록
    2. 장르 내에서 많이 재생된 노래를 먼저 수록
    3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
    """
    import heapq
    # genres[i] : 고유번호가 i인 노래의 장르
    # plays[i] : 고유번호가 i인 노래가 재생된 횟수
    song_p = defaultdict(int)
    song_i = defaultdict(list)
    for i in range(len(genres)):
        g = genres[i];p = plays[i];
        song_p[g] += p
        heapq.heappush(song_i[g], (-p, i))
    play = []
    for key, value in song_p.items():
        heapq.heappush(play, (-value, key))
    while play:
        p, g = heapq.heappop(play)
        for i in range(2):
            if song_i[g]:
                answer.append(heapq.heappop(song_i[g])[1])


    return answer
