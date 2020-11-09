# 작성 날짜 : 20201109
# 작성자 : 김동우
# 문제 명 : 베스트 앨범
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 :장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
#           노래는 고유 번호로 구분, 노래를 수록하는 기준은 다음과 같다.
#           1. 속한 노래가 많이 재새된 장르 먼저 수록
#           2. 장르 내에서 많이 재생된 노래 먼저 수록
#           3. 재생 횟수가 같으면 고유 번호가 낮은 순으로 수록

# 시간 복잡도 : O(N) (clothes 리스트 검색)
'''
genres =  ["classic","classic", "pop", "classic","piano", "classic", "pop","pop","piano"]
plays = [800,500, 600, 150,100, 800, 2500 ,2500,10000]
'''
genres =  ["classic"]
plays = [1]

def solution(genres, plays):
    answer=[]
    albumList=[]
    albumSort=[]

    # albumList = [[장르명, 횟수, 인덱스],[장르명, 횟수, 인덱스],...]
    for num,i in enumerate(genres):
        a=[i,plays[num],num]
        albumList.append(a)
    compareMaxPlay=[0,0]
    albumList.sort(key=lambda x:(x[0],-x[1]))
    editedAlbumList=albumList

    # editedAlbumList는 플레이 횟수가 가장 높은 장르를 찾으면 그 장르의 play값을 다 0으로 만들고
    # 다음 플레이 횟수가 높은 장르를 구할수 있게 한다.
    # 그 결과 albumSort에 플레이 횟수가 높은 순으로 장르를 저장한다. ['pop','classic']
    # compareMaxPlay는 [장르명, max 플레이 횟수] 가 저장되는 리스트이다.
    for j in range(len(albumList)):
        compareMaxPlay[1]=0
        for i in range(len(editedAlbumList)):
            if compareMaxPlay[1]<editedAlbumList[i][1]:
                compareMaxPlay=[editedAlbumList[i][0],editedAlbumList[i][1]]
        # compareMaxPlay[1]이 0이면 모든 장르를 다 확인한 경우라 loop문을 빠져나온다.
        if compareMaxPlay[1]==0:
            break
        albumSort.append(compareMaxPlay[0])

        for i in range(len(editedAlbumList)):
            if editedAlbumList[i][0]==compareMaxPlay[0]:
                editedAlbumList[i][1]=0


    # 정답 구하는 알고리즘
    for albumName in albumSort:
        maxTwoAlbumCheck=0
        for num,i in enumerate(albumList):
            if i[0]==albumName and maxTwoAlbumCheck<2:
                answer.append(albumList[num][2])
                maxTwoAlbumCheck+=1
    return answer

print(solution(genres,plays))