# 팰린드롬 : 앞뒤를 뒤집어도 똑같은 문자열
# 부분 문자열(Substring) 중 가장 긴 팰린드롬의 길이를 return하는 solution 함수를 완성하라.
# 문자열의 길이는 최대 2500 시간 복잡도는 n^2까지 가능

'''

abba : 4 
abab : 3
cabcfasafcba : 11
1. 한 글자씩 stack에 넣는다. 
2. 만약 다다음 글자가 지금 stack의 top과 같다면 stack을 복사해놓는다.
2-1. 동시에 복사해놓은 stack을 2번 pop한다.
2-2. count(answer) = 3으로 설정
3. 만약 복사해놓은 stack의 top과 다음 글자가 같다면 계속 pop하고 count+=2를 한다.
3-1. 만약 top과 다음 값이 다르다면 max와 비교해서 if count>max: max=count, count=0

'''
import copy

def solution(s):
    answer = 1
    stack = []
    
    for i,v in enumerate(s):
        stack.append(v)
    
        if len(s) > i+2:
            if s[i+2] == v:
                s1=copy.deepcopy(stack)
                s1.pop()
                count=3
                if len(s1)!=0 and i+3<len(s):
                    for inner_i in range(i+3,len(s)):
                        if s1[-1]==s[inner_i]:
                            count+=2
                            s1.pop()
                        else:
                            break
                if count > answer:
                    answer = count
        if len(s)>i+1:
            if s[i+1]==v:
                s2=copy.deepcopy(stack)
                s2.pop()
                count=2
                if len(s2)!=0 and i+2<len(s):
                    for inner_i in range(i+2,len(s)):
                        if s2[-1]==s[inner_i]:
                            count+=2
                            s2.pop()
                        else:
                            break
                if count > answer:
                    answer = count    
                        
    return answer