# 작성일자 : 20210305
# 문제명 : 단어 퍼즐

# +++++++++++++++++++++++++++++. 
# 아니 왜 프로그래머스 환경에서는 답이 3이 나오는가?
#++++++++++++++++++++++++++++++.
# 문제 요약 :
# 1. 문자열 리스트와 목표 문자열이 주어진다.
# 2. 문자열 리스트 내에 있는 단어들로 목표 문자열을 만들 수 있는 지 확인하고
# 3. 최소 몇개의 문자열을 사용해야 하는 지 반환하라

# 문제 풀이 : 백트래킹 사용하는 것
# 1. 각 과정은 똑같다. 다만 백트래킹으로 모든 경우를 확인하고
# 2. 범위 벗어나면 가지치기 하는 것을 넣자. 


def backtracking(i,copyedT,answer,strs):
    if copyedT=="":
        answerList.append(answer)
        return

    if i not in copyedT:
        return
    else:
        index=copyedT.find(i)
        copyedT=copyedT[:index]+copyedT[index+len(i):]
        answer+=1

    for str1 in strs:
        backtracking(str1,copyedT,answer,strs)

def solution(strs, t):
    strs.sort(reverse=True)
    global answerList
    answerList=[]
    for i in strs:
        backtracking(i,t,0,strs)

    if not answerList:
        print(-1)
        return -1
    else:
        return min(answerList)

if __name__=="__main__":
    strs=["ba", "an", "nan", "ban", "n"]
    t=["banana"]

    solution(strs,t)