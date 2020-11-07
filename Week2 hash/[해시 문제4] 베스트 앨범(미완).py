# 작성 날짜 : 20201107
# 작성자 : 김동우
# 문제 명 : 베스트 앨범
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 :장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
#           노래는 고유 번호로 구분, 노래를 수록하는 기준은 다음과 같다.
#           1. 속한 노래가 많이 재새된 장르 먼저 수록
#           2. 장르 내에서 많이 재생된 노래 먼저 수록
#           3. 재생 횟수가 같으면 고유 번호가 낮은 순으로 수록
# 설계 : 
'''
방법 1
1. 먼저 앨범의 순서를 구해야 한다. plays에서 max인 앨범을 albumList에 추가하고 장르별로 plays의 값을 0으로 만들어준다.

'''
# 시간 복잡도 : O(N) (clothes 리스트 검색)

def solution(genres, plays):
    answer = []
    ansDic={}
    max= plays[0]


    for num,i in enumerate(genres):
       ansDic[i]=[]

    for num,i in enumerate(genres):
        ansDic[i].append(plays[num])
        ansDic[i].append(num)

    pivot=0
    editedPlays=plays
    albumList=[]

    # 최고 엘범 찾기
    for j in range(ansDic):
        for num,i in enumerate(editedPlays):
            if max<i:
                max=i
                pivot=num
        albumList.append(genres[pivot])
        for i in genres:
            if i==genres[pivot]:
                editedPlays[i]=0
    # 여기까지 앨범고르기 성공
    # 그 다음으로 앨범별로 횟수가 많은 것에 따라 정렬하고 2개씩 순서대로 answer에 더하면 된다.
    for j in albumList:
        for key,value in ansDic.items():
            if j==i:
                for 


    return answer