# 작성일자 : 20210227
# 문제명 : 짝지어 제거하기
# 문제 요약 : 문자열이 있다. 이 문자열에서 짝지어 있는 알파벳 2개를 찾고 그 둘을 제거하고
# 앞 뒤로 문자열을 이어 붙인다. 문자열을 모두 제거한다면 짝지어 제거하는 것이 종료된다.
# 짝지어 제거하는 것을 모두 성공적으로 수행할 수 있다면 1 아니면 0을 리턴하시오
# 문자열의 길이가 1,000,000 이라서 O(N) or (Nlog_2 N)에 통과할 수 있어야 한다.

# 문제 풀이 1 : 제거할 수 있는 것을 확인하는 수학식을 생각해야 한다.  사용해보자.
# 중간에 안 되는 조건이 있는 지 확인을 하고 거기에서 멈춰야 한다. 중간에 대칭이 되는 지 확인을 해야 한다.
# 1. abba 는 되지만 abcabc는 안된다. abcabccbacba abbbbcaaca,  abccbbbcaaca 
# 2. 문자열을 1번 쭉 지워보고 이 문자열에 대해서 대칭인지 확인한기
# 3. 

def solution(string):
    # 1. 문자열에서 각 문자열이 2개씩 있는 지 확인한다. 없으면 x
    checkHash={}
    string1=[]
    for i in string:
        string1.append(i)
    for i in range(len(string1)):
        if checkHash.get(string1[i],0)==0:
            checkHash[string1[i]]=1
        else:
            checkHash[string1[i]]+=1
    for i in checkHash.values():
        if i%2==1:
            return 0
    for i in range()
    
    while(string1):
        if index1>=len(string1):
            break
        # 제거하는 방법을 다르게 해야한다.
        if index1!= 0 and string1[index1]==string1[index1-1]:
            string1[index1]=0
            string1[index1-1]=0
        index1+=1

    editedString=[]
    for i in string1:
        if i!=0:
            editedString.append(i)
    for i in range(len(editedString)):
        if editedString[i]!=editedString[-i-1]:
            return 0
    return 1


    


if __name__=="__main__":
    string1="cdcd"
    solution(string1)
