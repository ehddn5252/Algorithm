# 작성 날짜 : 20201107
# 작성자 : 김동우
# 문제 명 : 위장
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 : 옷과 옷 종류가 주어진다. 옷 set는 최소 한 종류이상이고, 같은 종류는 한번에 하나씩만 매칭할 수 있다. 
#            만들수 있는 옷 세트의 수 구하기
# 설계 : 
'''
방법 1
여기서 안입는 것도 옷 종류 중 하나로 쳐야한다. 그리고 아예 안입는 경우의 수를 마지막에 빼야 한다.
1. 종류당 옷의 개수를 정한다.
2. 종류당 옷의 개수+ 1(안입는경우)를 answer에 곱한다.
3. 아예 안 입는 경우 1개를 뺀다.
'''
# 시간 복잡도 : O(N) (clothes 리스트 검색)

def solution(clothes):
    answer = 1
    answerDictionary = {}
    # 해시 초기화
    for i in clothes:
        answerDictionary[i[1]] = 0
    # 각 종류에 따라 해시값을 추가해준다.
    for i in clothes:
        answerDictionary[i[1]] += 1
    # 각 종류당 +1한 값을 answer에 곱해준다.
    for value in answerDictionary.values():
        answer*=(value+1)
    # 아예 아무것도 안 입는 경우 하나를 뺀다.
    answer -= 1
    return answer
