# 작성 날짜 : 20201116
# 작성자 : 유 승 민
# 문제 명 : 나이 순 정렬
# 문제 유형: 정렬
"""
- 풀이 1 

가입 사람들의 데이터를 해쉬로 저장

키는 이름, 값은 나이,가입순서
"""

def solution():
    n = int(input())
    ageHash = {}
    indexHash = {}

    for i in range(n):
        # 가입 정보를 해쉬로 저장
        member = list(input().split(" "))
        ageHash[ member[1]] = int(member[0])
        indexHash[ member[1] ] = i
    
    ls = sorted(ageHash.items(), key=lambda x: x[1])
    print(ls)

    sameLs = []
    sameIndex = 0
    pivot = ""
    for i in range(n):
        if (i < n-1):
            pivot = ls[i+1][1]
        else:
            pivot = 0
        # 값이 같은 구간의 시작을 구분하기 위해 len(sameLs) == 0 조건도 넣는다.)
        if (ls[i][1] == pivot):
            # sameLs에 이름과 가입순서를 리스트로 추가한다.
            sameLs.append(( ls[i][0], indexHash[ls[i][0]] ))
        if (ls[i][1] != pivot and len(sameLs) != 0):
            sameLs.append(( ls[i][0], indexHash[ls[i][0]] ))
            sameLs = sorted(sameLs, key=lambda x: x[1])
            lenLs = len(sameLs)
            for i in range(lenLs):
                ls[lenLs-(i+1)] = sameLs[i]
            sameLs = []

    for i in range(n):
        print(ls[i][1], ls[i][0])
    

solution()
    