# 작성 날짜 : 20201105
# 작성자 : 김동우
# 문제 명 : 완주하지 못한 선수
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 : 리스트인 participant와 completion을 대조하여 completion에 없는 participant인원을 찾아라
# 설계 : 
'''
1. 해시를 answerDictionary라는 dictionary에 초기화한다.
2. completion의 수만큼 해시값을 더해준다. answerDictionary[i]+=1
3. participant의 수만큼 해시값을 빼준다. answerDictionary[i]-=1
[결과] 4. 빼고 남은 해시 값이 -1인 것이 답이다. if answerDictionary[i]==-1: return i
'''
# 시간 복잡도 : O(N)  (for문 1개 돌림)

def solution(participant, completion):
    answerDictionary = {}
    # 해시 초기화
    for i in participant:
        answerDictionary[i]=0
    # completion의 수만큼 해시값을 더해준다.
    for i in completion:
        answerDictionary[i]+=1
    # participant의 수만큼 해시값을 빼준다.
    for i in participant:
        answerDictionary[i]-=1
    # 만약 빼고 맨 마지막에 남은 해시 값이 -1인 경우에 그 사람이 마나톤을 완주 못한 사람이다.
        if answerDictionary[i]==-1:
            return i

