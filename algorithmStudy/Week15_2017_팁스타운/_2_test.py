# 작성일자 : 20210305
# 문제명 : 단어 퍼즐

# 문제 요약 :
# 1. 문자열 리스트와 목표 문자열이 주어진다.
# 2. 문자열 리스트 내에 있는 단어들로 목표 문자열을 만들 수 있는 지 확인하고
# 3. 최소 몇개의 문자열을 사용해야 하는 지 반환하라

# 문제 풀이 dp에 문자열을 저장하고 
import copy

def solution(strs, t):
    answer=0
    answersaved=0
    strs.sort(reverse=True)
    copyedT=copy.deepcopy(t)
    while copyedT!="":
        answersaved=answer
        for i in strs:
            print(copyedT)
            if copyedT.startswith(i):
                copyedT=copyedT[len(i):]
                answersaved=answer
                answer+=1
                break
        if answer==answersaved:
            return -1
    print(f'len(copyedT): {len(copyedT)} and copyedT = {copyedT}')
    print(answer)
    return answer

if __name__=="__main__":
    strs=["ba","na","n","a"]
    t="banana"
    solution(strs,t)