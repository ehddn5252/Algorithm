# 작성 날짜 : 20201107
# 작성자 : 김동우
# 문제 명 : 전화번호 목록
# 문제 유형: 해시는 값을 key value로 저장하는 형태이다.
# 문제 요약 : 전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인 경우가 있다면 false 아니면 true를 반환한다.
# 설계 : 
'''
방법 2 
phone_book을 2중 for문으로 돌려서 모두 비교한다.
1. phone_book을 오름차순으로 정렬한다. 오름차순으로 정렬하면 맨 앞자리가 같은 것이 붙어있을 것이다..
2. 맨 앞자리를 바로 다음 것의 앞자리와 비교한다.
3. 그 다음것과 다르다면 바로 다음것으로 넘어간다. 
'''

# 시간 복잡도 : O(Nlog(N)) (정렬하는 시간 Nlog(N))

def solution(phone_book):
    answer = False
    # 오름차순 정렬
    phone_book.sort()
    # phone_book을 for문으로 한번 돌린다.
    for num,i in enumerate(phone_book):
        # num이 마지막이 되면 memory size를 벗어나기때문에 확인문을 넣는다.
        if num!=len(phone_book)-1:
            # 만약 접두어가 같다면 false리턴
            if phone_book[num+1].startswith(i)==True:
                return answer
    # 끝까지 돌았다면 True 리턴
    answer=True
    return answer