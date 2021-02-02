# 작성일 : 20210106
# 작성자 : 김동우
# 문제명 : 네트워크
# 문제 요약 :

networkList=[]
def solution(n, computers):
    answer=0
    flag=1
    for _ in range(n):
        networkList.append(0)
    
    for computer in computers:
        for index,value in enumerate(computer):
            if value==1 and networkList[index]!=0:
                changeValue=networkList[index]
                for i in range(len(networkList)):
                    if networkList[i]==changeValue:
                        networkList[i]=flag
            elif value==1 and networkList[index]==0:
                networkList[index]=flag
        flag+=1
    setList=set(networkList)
    ansList=setList
    answer=len(ansList)
    return answer

