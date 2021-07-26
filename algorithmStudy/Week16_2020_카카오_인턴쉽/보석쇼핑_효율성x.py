# 작성 일자 : 20210312
# 문제명 : 보석 쇼핑

# 문제 요약 : 모든 보석을 한종류씩 포함하게 하는 열의 최소 길이를 구하라
# 문제 해설 : 
# 2차원 dp를 사용해서 10만 * 10만 은 너무 오래 걸린다.


def solution(gems):
    answerList = []
    for outerIndex,_ in enumerate(gems):
        gemsSet=set(gems)
        start=outerIndex
        for innerIndex in range(start,len(gems)):
            if gems[innerIndex] in gemsSet:
                gemsSet.remove(gems[innerIndex])
            if not gemsSet:
                if innerIndex-outerIndex==len(set(gems))-1:
                    return [outerIndex+1,innerIndex+1]
                answerList.append([outerIndex+1,innerIndex+1])
        
        #print(answerList)

    answerList.sort(key=lambda x:(x[1]-x[0],x[0]))
    return answerList[0]


if __name__=="__main__":
    gems=["AA", "AB", "AC", "AA", "AC"]
    solution(gems)
