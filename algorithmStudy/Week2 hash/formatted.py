# 작성 날짜 : 20201113
# 작성자 : 김동우
# 문제 명 : 베스트 앨범
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 :장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
#           노래는 고유 번호로 구분, 노래를 수록하는 기준은 다음과 같다.
#           1. 속한 노래가 총 재생수가 많은 장르 먼저 수록
#           2. 장르 내에서 많이 재생된 노래 먼저 수록
#           3. 재생 횟수가 같으면 고유 번호가 낮은 순으로 수록

# 시간 복잡도 : O(N^2)
# 고민 : 예외가 무엇인지 확인해야 한다. -> 문제 이해를 잘못함 해결(20201113)


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    albumList = []
    albumSort = []

    # albumList = [[장르명, 횟수, 인덱스],[장르명, 횟수, 인덱스],...]
    for num, i in enumerate(genres):
        a = [i, plays[num], num]
        albumList.append(a)

    albumList.sort(key=lambda x: (x[0], -x[1]))
    # if 장르면 그 장르에 저장한다.
    # 플레이 횟수의 합을 compareMaxPlay에 저장한다.
    compareMaxPlay = {}
    for album in albumList:
        compareMaxPlay[album[0]] = 0

    for album in albumList:
        compareMaxPlay[album[0]] += album[1]
    # album 재생수가 높은 순으로 sort albumSort = [(POP,5000),(classic,2000),(ahl,1000)...]
    albumSort = sorted(compareMaxPlay.items(), key=lambda x: -x[1])

    # 정답 구하는 알고리즘
    for albumName in albumSort:
        maxTwoAlbumCheck = 0
        for num, i in enumerate(albumList):
            if i[0] == albumName[0] and maxTwoAlbumCheck < 2:
                answer.append(albumList[num][2])
                maxTwoAlbumCheck += 1
    return answer
