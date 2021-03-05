# 작성일자 : 20210227
# 문제명 : 짝지어 제거하기
# 문제 요약 : 문자열이 있다. 이 문자열에서 짝지어 있는 알파벳 2개를 찾고 그 둘을 제거하고
# 앞 뒤로 문자열을 이어 붙인다. 문자열을 모두 제거한다면 짝지어 제거하는 거이 종료된다.
# 짝지어 제거하는 것을 모두 성공적으로 수행할 수 있다면 1 아니면 0을 리턴하시오
# 문자열의 길이가 1,000,000 이라서 1번만에 통과할 수 있어야 한다.
# 문제 풀이 :
# 1. 문자열에서 각 문자열이 2개씩 있는 지 확인한다. 없으면 x
# 2. index1에 있는 문자와 index1+1에 있는 문자가 같은 지 확인한다.
# 3. 만약 같다면 지우고 다음 차례를 확인한다. 

def solution(string):
    # 1. 문자열에서 각 문자열이 2개씩 있는 지 확인한다. 없으면 x
    string1=[]
    for i in string:
        string1.append(i)
    checkHash={}
    for i in range(len(string1)):
        if checkHash.get(string1[i],0)==0:
            checkHash[string1[i]]=1
        else:
            checkHash[string1[i]]+=1
    for i in checkHash.values():
        if i%2==1:
            return 0

    index1=0
    while(string1):
        if index1==len(string1):
            return 0
        # 동일 문자열쌍 제거
        if index1!= 0 and string1[index1]==string1[index1-1]:
            string1[index1-1:index1+1]=""
            index1-=1
        else:
            index1+=1
    return 1

if __name__=="__main__":
    string1="baabaa"
    solution(string1)