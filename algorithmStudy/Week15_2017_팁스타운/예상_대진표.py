# 작성일자 : 20210305
# 문제명 : 예상 대진표

# +++++++++++++++++++++++++++++. 
# 아니 왜 프로그래머스 환경에서는 답이 3이 나오는가?
#++++++++++++++++++++++++++++++.
# 문제 요약 :
# 1. 게임 대회가 개최 되었다. 1번은 2번, 3번은 4번 ... , 과 대결한다.
# 2. a번과 b번은 몇 번째 라운드에서 붙게 될까?
# 문제 풀이 :
def solution(n,a,b):
    answer = 1
    while True:
        if (a%2==1 and a+1==b) or (b%2==1 and b+1==a):
            return answer
        else:
            answer+=1
        if a>1 and a%2==0:
            a//=2
        elif a%2==1:
            a=a//2+1
        if b>1 and b%2==0:
            b//=2
        elif b%2==1:
            b=b//2+1
    return answer


if __name__=="__main__":
    n=8
    a=4
    b=7
    solution(n,a,b)