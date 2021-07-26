# 작성 일자 : 20210312
# 문제명 : 보석 쇼핑

# 문제 요약 : 모든 보석을 한종류씩 포함하게 하는 열의 최소 길이를 구하라
# 2차원 dp를 사용해서 10만 * 10만 은 너무 오래 걸린다.
# 문제 해설 :
# 1. 모든 종류의 보석 리스트를 얻는다.
# 2. 맨 처음부터 보석을 추가한다.
# 3. 모든 종류의 종류가 모였을 때 앞에서부터 없앤다.
# 4. 어디까지 줄여야하나? 모든 경우가 하나씩일때까지?


# 지금 문제점 : test case 1번에서 current가 4인데도 움직이지 않는다.

def solution(gems):
    answerList = []
    gemHash={}
    genKinds=0
    currentKinds=0
    # gem해쉬를 만든다
    for _,value in enumerate(gems):
        if value not in gemHash:
            gemHash[value]=0
            genKinds+=1
    #start부터 end까지 보석이 있는 지 확인한다.
    start =0
    # 모든 보석 종류가 하나씩있으면 멈춥니다.
    end=0
    endFlag=True
    # 만약 end가 gems보다 커지면 나가진다.
    while end<len(gems) and start<=end:
        # end가 움직이는 조건
        if endFlag:
            if gemHash[gems[end]]==0:
                currentKinds+=1
            gemHash[gems[end]]+=1
            if currentKinds==genKinds:
                #if end-start+1==genKinds:
                #    return [start+1,end+1]
                answerList.append([start+1,end+1])
                endFlag=False
            else:
                end+=1
        else:
            endFlag=True
            if gemHash[gems[start]]==1:
                currentKinds-=1
            else:
                answerList.append([start+1,end+1])
            gemHash[gems[start]]-=1
            start+=1

    answerList.sort(key=lambda x:(x[1]-x[0],x[0]))
    return answerList[0]