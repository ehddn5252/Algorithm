# 작성 일자 : 20210312
# 문제명 : 보석 쇼핑

# 문제 요약 : 모든 보석을 한종류씩 포함하게 하는 열의 최소 길이를 구하라
# 2차원 dp를 사용해서 10만 * 10만 은 너무 오래 걸린다.
# 정확도는 맞음



def solution(gems):
    answerList = []
    gemsHash={}
    for gem in gems:
        gemsHash[gem]=0
    
    for i in range(gemsHash):
        gemsHash


    gemsSet=set(gems)
    for outerIndex,value in enumerate(gems):
        if gems==0:

        
    #print(answerList)

    answerList.sort(key=lambda x:(x[1]-x[0],x[0]))
    return answerList[0]



if __name__=="__main__":
    gems=["AA", "AB", "AC", "AA", "AC"]
    solution(gems)